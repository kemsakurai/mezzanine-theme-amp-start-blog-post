from mezzanine.conf import register_setting

###########################
# FOR AMO SETTINGS #
###########################
register_setting(
    name="TEMPLATE_ACCESSIBLE_SETTINGS",
    description=("Sequence of setting names available within templates."),
    editable=False,
    default=("AMP_GOOGLE_ADS_CLIENT_ID",
             "AMP_GOOGLE_ADS_SLOT_ID",
             "AMP_GOOGLE_TAG_MANGER_ID",
             ),
    append=True,
)
