from five import grok
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.interfaces import IVocabularyFactory
from zope.component import getUtility
from z3c.formwidget.query.interfaces import IQuerySource

from ploneun.vocabularies import MessageFactory as _

class AsiaPacific(grok.GlobalUtility):
    grok.name('ploneun.vocabularies.countries.asiapacific')
    grok.implements(IVocabularyFactory)

    # Asia-Pacific Countries
    _terms = SimpleVocabulary(
    [SimpleTerm(value=u'AF',
                title=_(u'Afghanistan')),
    SimpleTerm(value=u'AU',
                title=_(u'Australia')),
    SimpleTerm(value=u'BD',
                title=_(u'Bangladesh')),
    SimpleTerm(value=u'BT',
                title=_(u'Bhutan')),
    SimpleTerm(value=u'BN',
                title=_(u'Brunei')),
    SimpleTerm(value=u'KH',
                title=_(u'Cambodia')),
    SimpleTerm(value=u'CN',
                title=_(u'China')),
    SimpleTerm(value=u'HK',
                title=_(u'Hong Kong')),
    SimpleTerm(value=u'IN',
                title=_(u'India')),
    SimpleTerm(value=u'ID',
                title=_(u'Indonesia')),
    SimpleTerm(value=u'IR',
                title=_(u'Iran')),
    SimpleTerm(value=u'JP',
                title=_(u'Japan')),
    SimpleTerm(value=u'LA',
                title=_(u'Lao PDR')),
    SimpleTerm(value=u'MO',
                title=_(u'Macao')),
    SimpleTerm(value=u'MY',
                title=_(u'Malaysia')),
    SimpleTerm(value=u'MV',
                title=_(u'Maldives')),
    SimpleTerm(value=u'MN',
                title=_(u'Mongolia')),
    SimpleTerm(value=u'MM',
                title=_(u'Myanmar')),
    SimpleTerm(value=u'NP',
                title=_(u'Nepal')),
    SimpleTerm(value=u'NZ',
                title=_(u'New Zealand')),
    SimpleTerm(value=u'KP',
                title=_(u'North Korea')),
    SimpleTerm(value=u'PK',
                title=_(u'Pakistan')),
    SimpleTerm(value=u'PH',
                title=_(u'Philippines')),
    SimpleTerm(value=u'SG',
                title=_(u'Singapore')),
    SimpleTerm(value=u'KR',
                title=_(u'South Korea')),
    SimpleTerm(value=u'LK',
                title=_(u'Sri Lanka')),
    SimpleTerm(value=u'TW',
                title=_(u'Taiwan')),
    SimpleTerm(value=u'TH',
                title=_(u'Thailand')),
    SimpleTerm(value=u'TL',
                title=_(u'Timor-Leste')),
    SimpleTerm(value=u'VN',
                title=_(u'Vietnam')),
    ]
    )

    def __call__(self, context):
        return self._terms
