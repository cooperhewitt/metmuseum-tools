# metmuseum-tools

## python

### metmuseum.collection

For example, this:

	import sys
	import pprint
	import metmuseum

	q = sys.argv[1:]
	q = " ".join(q)

	col = metmuseum.collection()
	links = col.search(q)

	for url in links:

		data = col.extract(url)

		print url
		print pprint.pformat(data)
		print "--"
	
Would print:

	http://www.metmuseum.org/collection/the-collection-online/search/547775
	{u'Accession Number': u'1997.375',
	 'Chat': u"This extraordinarily lifelike animal head was once part of a hippopotamus statue about three feet in length. Comparisons with other sculptures from the period indicate that it was created during the reign of Amenhotep III. The seated statues that the king dedicated to the goddess Sakhmet are well known (); their feline heads display hollow sinewed cheeks and knobby facial bones similar to those on the hippo. This head may have come from Amenhotep's mortuary temple on the west bank of the Nile opposite modern Luxor. This temple was mostly dismantled in ancient times, but the site is marked by two colossal statues of the king known as the colossi of Memnon.Excavators have found another, even larger, hippo statue, also of Egyptian alabaster, at the site. Together with hundreds of other sculptures\u2014many of them representing deities in animal form\u2014the hippos would have served in rituals procuring godlike status for the king. On the underside of the animal's jaw is an ancient drill hole. It may have been made for a metal support (the head is heavy) or for the insertion of the hook of a harpoon during a ritual hippopotamus hunt. Traces of paint, which are preserved in furrows at the sides of the mouth, may have been added at such a performance, transforming the beneficial white animal into a dangerous red one.",
	 u'Credit Line': u'Purchase, Harris Brisbane Dick Fund, Lila Acheson Wallace Gift, Gift of Henry Walters, by exchange, Ludlow Bull Fund, Beatrice Cooper Gift, and funds from various donors, 1997',
	 u'Date': u'ca. 1390\u20131352 B.C.',
	 u'Dimensions': u'H. 14 cm (5 1/2 in); W. 12.2 cm (4 13/16 in); D. from back to jaw 15.2 cm (6 in)',
	 u'Dynasty': u'Dynasty 18',
	 u'Geography': u'From Egypt',
	 u'Medium': u'Travertine (Egyptian alabaster) with traces of gesso and red pigment',
	 u'Period': u'New Kingdom',
	 u'Reign': u'reign of Amenhotep III'}
	--
	http://www.metmuseum.org/collection/the-collection-online/search/544227
	{u'Accession Number': u'17.9.1',
	 'Chat': u'This well-formed statuette of a hippopotamus (popularly called "William") demonstrates the Egyptian artist\'s appreciation for the natural world. It was molded in faience, a ceramic material made of ground quartz. Beneath the blue-green glaze, the body was painted with the outlines of river plants, symbolizing the marshes in which the animal lived.The seemingly benign appearance that this figurine presents is deceptive. To the ancient Egyptians, the hippopotamus was one of the most dangerous animals in their world. The huge creatures were a hazard for small fishing boats and other rivercraft. The beast might also be encountered on the waterways in the journey to the afterlife. As such, the hippopotamus was a force of nature that needed to be propitiated and controlled, both in this life and the next. This example was one of a pair found in a shaft associated with the tomb chapel of the steward Senbi II at Meir, an Upper Egyptian site about thirty miles south of modern Asyut. Three of its legs have been restored because they were purposely broken to prevent the creature from harming the deceased. The hippo was part of Senbi\'s burial equipment, which included a canopic box (also in the Metropolitan Museum), a coffin, and numerous models of boats and food production.',
	 u'Credit Line': u'Gift of Edward S. Harkness, 1917',
	 u'Date': u'ca. 1961\u20131878 B.C.',
	 u'Dimensions': u'L. 20 cm (7 7/8 in.); W. 7.5 cm (2 15/16 in.); H. 11.2 cm (4 7/16 in.)',
	 u'Dynasty': u'Dynasty 12, first half',
	 u'Geography': u'From Egypt, Middle Egypt, Meir (Mir), Tomb B no. 3  of the nomarch Senbi II, pit 1 (steward Senbi), Khashaba 1910',
	 u'Medium': u'Faience',
	 u'Period': u'Middle Kingdom',
	 u'Reign': u'Senwosret I to Senwosret II'}
	--
