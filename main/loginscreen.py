from kivy.uix.relativelayout import RelativeLayout
import crypt
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty


# ----- Classe generale del layout ----------------------------------------------------------------------------------- #
class LoginScreen(Screen):
    mccm = ObjectProperty(None)
    pass


class LoginContainer(RelativeLayout):
    def __init__(self, **kwargs):
        super(LoginContainer, self).__init__(**kwargs)
        self.loginuser = 'AdS9O3DYbGQ/I'
        self.loginpass = 'Ads/OqaDRP7pE'

    def do_login(self, user, password):
        if str(crypt.crypt(user, user)) != self.loginuser and str(crypt.crypt(password, user)) != self.loginpass:
            self.lsc_user.text = ''
            self.lsc_password.text = ''
            self.lsc_warning.opacity = 0
            # self.setting_screen.check_connection_status.update()
            # self.setting_screen.list_connection_button.update()
            self.mccm_login.mccm.switch_to(self.mccm_login.mccm.mccm_settings)
        else:
            self.ids.warning.opacity = 1
