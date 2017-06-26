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

register_setting(
    name="AMP_GOOGLE_ADS_CLIENT_ID",
    description="GOOGLE ADS CLIENT ID for AMP",
    editable=True,
    default="",
)

register_setting(
    name="AMP_GOOGLE_ADS_SLOT_ID",
    description="GOOGLE ADS SLOT ID for AMP",
    editable=True,
    default="",
)

register_setting(
    name="AMP_GOOGLE_TAG_MANGER_ID",
    description="GOOGLE TAG MANGER ID for AMP",
    editable=True,
    default="",
)
