from five import grok
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.interfaces import IVocabularyFactory
from zope.component import getUtility
from z3c.formwidget.query.interfaces import IQuerySource

from ploneun.vocabularies import MessageFactory as _

class Types(grok.GlobalUtility):
    grok.name('ploneun.vocabularies.organizations.types')
    grok.implements(IVocabularyFactory)

    _terms = SimpleVocabulary(
            [SimpleTerm(value=u'government', 
                        title=_(u'Government')),
            SimpleTerm(value=u'ngo', 
                       title=_(u'NGO')),
            SimpleTerm(value=u'private_sector', 
                       title=_(u'Private Sector')),
            SimpleTerm(value=u'academic', 
                       title=_(u'Academic/Research')),
            SimpleTerm(value=u'international', 
                       title=_(u'International Organization')),
            SimpleTerm(value=u'other', 
                       title=_(u'Other')),
             ])

    def __call__(self, context):
        return self._terms

class Areas(grok.GlobalUtility):
    grok.name('ploneun.vocabularies.organizations.areas')
    grok.implements(IVocabularyFactory)

    _terms = SimpleVocabulary(
        [SimpleTerm(value=u'policy', 
                    title=_(u'Policy')),
         SimpleTerm(value=u'regulatory', 
                    title=_(u'Regulatory')),
         ]
        )

    def __call__(self, context):
        return self._terms



