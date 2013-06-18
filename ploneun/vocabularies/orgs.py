from zope import schema
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

types = SimpleVocabulary(
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
