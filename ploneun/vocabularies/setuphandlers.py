from collective.grok import gs
from ploneun.vocabularies import MessageFactory as _

@gs.importstep(
    name=u'ploneun.vocabularies', 
    title=_('ploneun.vocabularies import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('ploneun.vocabularies.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
