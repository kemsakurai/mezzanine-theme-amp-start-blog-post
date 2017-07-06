from mezzanine.conf import register_setting

###########################
# FOR AMO SETTINGS #
###########################
register_setting(
    name="TEMPLATE_ACCESSIBLE_SETTINGS",
    description=("Sequence of setting names available within templates."),
    editable=False,
    default=("AMP_GOOGLE_ADS_CLIENT_ID_TOP",
             "AMP_GOOGLE_ADS_SLOT_ID_TOP",
             "AMP_GOOGLE_ADS_CLIENT_ID_BOTTOM",
             "AMP_GOOGLE_ADS_SLOT_ID_BOTTOM",
             "AMP_GOOGLE_TAG_MANGER_ID",
             "AMP_TWITTER_ACCOUNT_NAME",
             "AMP_GITHUB_USER_NAME",
             ),
    append=True,
)

register_setting(
    name="AMP_GOOGLE_ADS_CLIENT_ID_BOTTOM",
    description="GOOGLE ADS CLIENT ID for AMP",
    editable=True,
    default="",
)

register_setting(
    name="AMP_GOOGLE_ADS_SLOT_ID_BOTTOM",
    description="GOOGLE ADS SLOT ID for AMP",
    editable=True,
    default="",
)
register_setting(
    name="AMP_GOOGLE_ADS_CLIENT_ID_TOP",
    description="GOOGLE ADS CLIENT ID for AMP",
    editable=True,
    default="",
)

register_setting(
    name="AMP_GOOGLE_ADS_SLOT_ID_TOP",
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
register_setting(
    name="AMP_TWITTER_ACCOUNT_NAME",
    description="Twitter account name SNS link",
    editable=True,
    default="",
)

register_setting(
    name="AMP_GITHUB_USER_NAME",
    description="Github user name SNS link",
    editable=True,
    default="",
)
