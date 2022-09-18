# prebuilt kernel
TARGET_PREBUILT_KERNEL := device/bn/st18c10bnn/kernel

PRODUCT_COPY_FILES += \
    $(LOCAL_PATH)/recovery/init.recovery.mt8167.rc:root/init.recovery.mt8167.rc \
    $(LOCAL_PATH)/recovery/init.mt8167.usb.rc:root/init.mt8167.usb.rc 

$(call inherit-product, $(SRC_TARGET_DIR)/product/aosp_base.mk)
$(call inherit-product, $(SRC_TARGET_DIR)/product/core_64_bit.mk)

