from conans import ConanFile


class Medium(ConanFile):
    requires = "top/1.0.0@user/channel"

    def package_id(self):
        self.info.options["top"].bool_option = self.options["top"].bool_option

    # def package_id(self):
    #     self.info.requires["top"].full_package_mode()
