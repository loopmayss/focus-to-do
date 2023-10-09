from user_auth.register import Register

register = Register()
register.load_data_user_personal_or_student()
register.load_data_user_professional()

register.ask_for_information()

