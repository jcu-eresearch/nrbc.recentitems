from zope.i18nmessageid import MessageFactory
NrbcRecentChangesMessageFactory = MessageFactory('nrbc.portlet.recentitems')

def initialize(context):
    """Initializer called when used as a Zope 2 product."""

    # Register Plone skins directory
    from Products.CMFCore import DirectoryView
    GLOBALS = globals()
    DirectoryView.registerDirectory('skins', GLOBALS)

