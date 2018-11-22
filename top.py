from conans import ConanFile


class Top(ConanFile):
    options = {"bool_option": [True, False]}
    default_options = {"bool_option": True}
