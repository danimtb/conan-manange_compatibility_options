from conans import ConanFile


class Consumer(ConanFile):
    requires = "medium/1.0.0@user/channel"

    # def requirements(self):
    #     self.requires("top/1.0.1@user/channel", override=True)
