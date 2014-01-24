from flask.ext.login import LoginManager, login_user, UserMixin, login_required, logout_user, current_user
from app import app
import ldap

class User(UserMixin):
	# ident can be : stephane (name), or stephane@22...(mail) or...
	# the attribute correspond to the variable LDAP_ID
	def __init__(self, ident=None, number=None, password=None):
			
		# intialisation
		self.active = False
		self.admin = False
		
		if ident is not None :
			# ldap_id : uid=stephane
			self.ldap_id = app.config['LDAP_ID']+'='+ ident
		else :
			self.ldap_id = 'uidNumber=' + number
		
		# dn = ldid + basedn : uid=stephane,ou=users,dc=22...
		self.dn = self.ldap_id + ',' + app.config['LDAP_USERS'] + ',' + app.config['LDAP_BASE']
		
		ldapuri = 'ldap://' + app.config['LDAP_HOST']
		try:
			l = ldap.initialize(ldapuri)
		except ldap.LDAPError, e:
			print e.message['info']
			if type(e.message) == dict and e.message.has_key('desc'):
				print e.message['desc']
			else:
				print e
			sys.exit()
			
			self.active = False
		if password is not None:
			l.bind_s(self.dn, password)
		
		result = l.search_s(self.dn,ldap.SCOPE_BASE)
		self.active = True
		var = result[0][1]
		self.idnumber = 	var['uidNumber'][0]
		self.home = 		var['homeDirectory'][0]
		self.name = 		var['uid'][0]
		self.familyname = 	var['sn'][0]
		self.completname = 	var['cn'][0]
		self.img = 		var.get('jpegphoto')
		
		
		if result[0][1]['mail'] is not None:
			self.mails = result[0][1]['mail']
	
	def is_active(self):
		return self.active
	
	def is_admin(self):
		return self.admin
	
	def is_authenticated(self):
		return self.active

	def get_id(self):
		return self.name

	def __repr__(self):
		return self.completname