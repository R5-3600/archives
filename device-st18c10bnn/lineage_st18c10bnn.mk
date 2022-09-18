# Android defaults
$(call inherit-product, $(SRC_TARGET_DIR)/product/core_64_bit.mk)
$(call inherit-product, $(SRC_TARGET_DIR)/product/product_launched_with_o_mr1.mk)
$(call inherit-product, vendor/lineage/config/common_full_tablet_wifionly.mk)
$(call inherit-product, $(SRC_TARGET_DIR)/product/languages_full.mk)
$(call inherit-product, $(SRC_TARGET_DIR)/product/full_base.mk)

# Inherit from st18c10bnn device
$(call inherit-product, $(LOCAL_PATH)/device.mk)

PRODUCT_BRAND := nook
PRODUCT_DEVICE := st18c10bnn
PRODUCT_MANUFACTURER := nook
PRODUCT_NAME := lineage_st18c10bnn
PRODUCT_MODEL := BNTV650

PRODUCT_GMS_CLIENTID_BASE := android-nook
#TARGET_VENDOR := nook
#TARGET_VENDOR_PRODUCT_NAME := st18c10bnn
#PRODUCT_BUILD_PROP_OVERRIDES += PRIVATE_BUILD_DESC="st18c10bnn-user 8.1.0 O11019 1575971992 release-keys"

# Set BUILD_FINGERPRINT variable to be picked up by both system and vendor build.prop
#BUILD_FINGERPRINT := Nook/st18c10bnnxx/st18c10bnn:8.1.0/O11019/1575971992:user/release-keys
