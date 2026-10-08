[app]
title = Kopi Nusantara
package.name = kopinusantara
package.domain = org.kopi
source.dir = .
source.include_exts = py,png,jpg,kv,db
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 0
icon.filename = logo.png

android.permissions = INTERNET
android.api = 33
android.accept_sdk_license = True
android.ndk = 25b
android.minapi = 21
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 1
