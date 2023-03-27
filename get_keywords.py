
from sklearn.feature_extraction.text import TfidfTransformer
import spacy 

def tokenize(text):
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text.lower())
    return doc 

#temporary function for testing 
def example():
    text = 'iPhone 14 and iPhone 14 Plus - AppleAppleStoreMaciPadiPhoneWatchAirPodsTV & HomeEntertainmentAccessoriesSupport0+iPhone 14Local Nav Open MenuLocal Nav Close MenuOverviewSwitching to iPhoneSwitch from Android to iPhoneTech SpecsBuyiPhone 14Get credit toward an iPhone 14 when you trade in an eligible smartphone.Get credit toward an iPhone 14 when you trade in an eligible smartphone.*Shop iPhoneiPhone 14 and iPhone 14 PlusiPhone 14 and iPhone 14 PlusWonderfull.**Watch theiPhone 14filmWatch theiPhone 14eventViewiPhone 14 and iPhone 14 Plusin AROur longest battery life ever.Emergency SOSvia satellite.Epic Prolevel photos and videos.Big and bigger.BigiPhone 146.1and bigger.iPhone 14 Plus6.7iPhone 14 and iPhone 14 PlusBigiPhone 146.1and bigger.iPhone 14 Plus6.7Our longest battery life ever.Our longest battery life ever.Emergency SOSvia satellite.Epic Prolevel photos and videos.Big and bigger.iPhone 14 and iPhone 14 PlusWonderfull.**Watch theiPhone 14filmWatch theiPhone 14eventViewiPhone 14 and iPhone 14 Plusin ARDesignFive fantastic colorsBluePurpleMidnightStarlightBluePurpleMidnightStarlight(Product) RedVibrant SuperRetina XDR displayBeautifully durableaerospacegrade aluminumSails through spillswith water resistance1Ceramic Shieldis tougher than any smartphone glassBluePurpleMidnightStarlight(Product) RedVibrant SuperRetina XDR displayCeramic Shieldis tougher than any smartphone glassBeautifully durableaerospacegrade aluminumSails through spillswith water resistance10123Lock ScreenYour photo.Your font.Your widgets.Your iPhone.iOS 16 lets you customize your Lock Screen in fun new ways. Layer a photo to make it pop. Track your Activity rings. And see live updates from your favorite apps.App Tracking Transparency lets you decide which apps are allowed to track your activity  its just one example of how iPhone is designed to put you in control of what you share and who you share it withSafety FeaturesVital new safety features we hope youll never need.Emergency SOS via satellite.Peace of mind when youre off the grid.If you dont have cell service or WiFi, iPhone lets you text emergency services over satellite.2See how it works and what makes it all possibleSOSHow onearthdo youcommunicatevia satellite?Satellites are moving targets with low bandwidth. It can take minutes for messages to get through. Since every second counts, iPhone front-loads a few questions to assess your situation  just tap to respond. Then it shows you where to point to connect to a satellite.Once connected, iPhone automatically sends your answers, location, Medical ID (if set up), and battery level to a dispatcher.You must be outdoors with a clear view of the sky.Since satellites are moving rapidly through space, iPhone will show you where to point to maintain your connection  and avoid obstructions such as mountains and heavy foliage.Texting via satellite takes time.In ideal conditions, you can send a message in less than 15 seconds. Under light foliage, it can take more than a minute.Emergency SOS via satellite is included for free with iPhone 14 for two yearsWatch the video to see Emergency SOS via satellite in action.An infrastructure of innovation.Apple-designed components and software allow iPhone 14 antennas to connect to satellite frequencies. And since bandwidth is low, we created a compression algorithm that makes text messages three times smaller, speeding up communication.On the ground, we route your text message through a complex infrastructure to emergency service providers. Only some accept texts. For those that dont, weve set up emergency relay centers with Appletrained specialists who call for help on your behalf.Let friends know how remote you go.If youre on an adventure without cell service, you can now use Find My to share your location via satellite so friends and family know where you are.CloseCrash Detectioncalls for help when you cant.iPhone 14 can detect asevere car crash, then call 911 and notify your emergency contacts.3See how the tech in iPhone 14 recognizes a severe car crashCrash DetectionHow iPhonefeels, hears, and measures a crash.Sudden speed shiftsA new high gforce accelerometer senses extreme accelerations or decelerations up to 256 Gs.Abrupt changes in directionA high dynamic range gyroscope monitors drastic changes in a cars orientation.Laboratory crash testsWe developed advanced motion algorithms by performing head-on, rear-end, side-impact, and rollover crash tests.Cabin pressure changesThe barometer can detectpressure changes caused by deploying airbags.Loud sound levels of impactWhile youre driving, the microphone identifies the extreme sound levels of a collision. For privacy, all processing is done on your iPhone.Real-world crash dataWe used public crash data from accidents to make Crash Detection as accurate as possible.1 million hours of realworld driving and crash data helps iPhone recognize accidentsCloseBatteryA huge Plus for battery life.A hugePlusforGet our best battery life ever on iPhone 14 Plus.And awesome all-day battery life on iPhone 14.Up to26hoursvideo playback oniPhone 14 Plus4Up to20hoursvideo playback oniPhone 144Add a MagSafe charger for faster wireless charging5Display21% more screen.Now thats big.iPhone 14 Plus has a supersized Super Retina XDR display.6OLED technologydelivers incredible contrast for bright whites and true blacks.High resolution and color accuracymake everything look sharp and true to life.True Tonemakes your display easier on the eyesby adjusting to the ambient light.Looking for an even more advanced display?iPhone 14 Pro has Dynamic Island, a magical new way to interact with iPhone. And an AlwaysOn display, which keeps your important info at a glance.CameraCam-packed.Camera GalleryMoredetailed details.Morecolorful colors.Moreepic pics.A new Prolevel Main camera and improved image processing let you capture even more sensational shots in all kinds of light  especially low light.Up to2.5x better lowlight photoson the Main cameraUp to2x better lowlight photoson the Ultra Wide cameraSee how iPhone 14 helps you take your best shots yetCameraA new Main camera features a bigger sensor and a larger aperture that let in 49 percent more light.Tap the shutter and the new Photonic Engine goes beyond what the camera alone can do. It merges the best pixels from multiple exposures at an earlier stage than ever before. This preserves much more image data to deliver brighter, more lifelike colors and beautifully detailed textures in even lower light.Choose theUltra Wide camerato capture unique perspectives and way more of a sceneA brighter True Tone flashwith more consistent lightingNight modeautomatically kicks in for especially dark scenes so you get brighter, sharper photos.Up to2x fasterNightmodeexposureson the Main cameraSmart HDR 4recognizes up to four people in your shot and automatically refines contrast, lighting, and skin tone for each one.Portrait modeputs the focus on your subject by artfully blurring the background  and now the foreground, too.Want to take your photos even further?iPhone 14 Pro has a 48MP Main camera that delivers mindblowing detail. It also has a Telephoto camera so you can shoot beautiful closeups from far away.CloseWhen apps request access to your photos, iPhone lets you call the shots by sharing just the ones you want instead of your entire libraryAction ModeGo steady.Without Action modePausePlayReplayWith Action modeWhether youre filming while hiking up a rocky trail or chasing your kids through the park, try Action mode for smooth handheld videos.Cinematic ModeHome movies that look likeHollywdmovies.Cinematic mode automatically shifts focus to the most important subject in a scene, just like filmmakers do. And now you can record in 4K at 24 fps  the same frame rate you see in the movies.Highestquality videoin a smartphoneTrueDepthSelfies youll flip over.Snap your sharpest, most colorful close-ups and group shots, thanks to a new TrueDepth front camera with autofocus and a larger aperture.Up to2x betterlowlight photosSee how spectacular your selfies can lookSelfiesOn the count of three, say we. Now that the TrueDepth camera can automatically focus on multiple subjects at once, all your selfies  from stunning closeups to group shots  look their sharpest.And the larger aperture lets in lots more light, capturing brighter color and finer detail in low-light scenes.38% better lightgathering performancefor more detail and less noise inphotos and videosCloseThe TrueDepth camera and A15 Bionic also power Face ID, the most secure facial authentication in a smartphoneiPhone 14 uses 100% recycled gold wire in all its cameras to reduce mining of precious resourcesA15 Bionic.Fast that lasts.iPhone 14 has the same superspeedy chip thats in iPhone 13 Pro.A15 Bionic, with a 5core GPU, powers all the latest features and makes graphically intense games and AR apps feel ultrafluid.An updated internal design delivers better thermal efficiency, so you can stay in the action longer.The Secure Enclave in A15 Bionic protects personal information like your Face ID data, contacts, and moreeSIMSo long,SIM tray.eSIM makes things simple. Its an industry-standard technology that lets you activate your new iPhone or add carriers digitally. So youre calling and texting in no time.7And unlike a physical card, eSIM cant be removed if your iPhone is lost or stolen.eSIM lets you havemultiple phonenumbers and data planson one phoneTraveling is a breezeBefore you go, activate an eSIM for thecountry or regionyoure visitingLearn moreabout traveling with eSIMSee bothiPhone 14models in AR.Open this page in Safari on your iPhone or iPad.BluePurpleMidnightStarlight(Product) RedView iPhone 14 in ARView iPhone 14 Plus in ARPrivacy is built in.Check out the latest privacy features for iPhoneApple has a plan.See how all our products will be carbon neutral by 2030iOS 16. Personal is powerful.Explore the new features in iOS 16iPhone for all.Discover accessibility features like Voice Control for iPhoneTrade in your smartphone for credit.With Apple Trade In, you can get credit toward a new iPhone when you trade in an eligible smartphone.8Its good for you and the planet.Learn moreabout Apple trade inThe easiest way to upgrade to the latest iPhone.Join the iPhone Upgrade Program to get the latest iPhone every year, low monthly payments, and AppleCare+.9Learn moreabout iphone upgrade programStill have questions? Just ask.You wont find a better place to buy iPhone. We know about carriers, payment options, and more. And we make it easy to understand.Learn moreabout buying iPhoneSpecial carrier deals at AppleSave up to $800 on iPhone 14 after tradein.10Get up to $800credit after trade-inGet $300-$770credit after trade-inGet up to $400credit after trade-inGet up to $800credit after trade-inShop iPhone 14Our Specialists can helpyou shop  online or in store.Connect with an iPhone SpecialistHave even more funwith your iPhone.TheApp Storeoffers nearly 1.8 million apps  all held to the highest privacy standards.Learn moreabout The App StoreApple Fitness+for thousands of workouts, even if you dont yet have an Apple Watch.11Learn moreabout Apple Fitness+Apple Onebundles up to six services for music, movies, games, and more in one easy subscription.Learn moreabout Apple OneMagSafecases and wallets let you snap on fun colors. MagSafe also gives you faster wireless charging.5Learn moreabout MagSafe20W USB-C Power Adapterlets you plug in for even faster charging in a compact, easytocarry size.Learn moreabout 20W USB-C Power AdapterApple Watchlets you ping your iPhone with a tap if youve misplaced it. And iPhone lets you find your Apple Watch just as easily.Learn moreabout Apple WatchAirPods Proplace sound all around you with Personalized Spatial Audio. Engrave the case for free, only at Apple.Learn moreabout AirPods ProAirTag.Attach one to your keys. Put another in your backpack. If theyre lost, just use the Find My app.Learn moreabout AirTagA Guided Tour ofiPhone 14 &iPhone 14 ProWatch the filmWhich iPhone is right for you?NewiPhone 14 ProThe ultimate iPhone.BuyLearn moreViewiPhone 14 Proin AR6.7 or 6.1Super Retina XDRdisplay6ProMotion technologyAlways-On displayDynamic IslandA new way tointeract with iPhoneEmergency SOSvia satellite2Emergency SOSCrash DetectionPro camerasystem48MP MainUltra WideTelephotoPhotonic Engine for incredible detail and colorAutofocuson TrueDepthfront cameraAction mode smooths out shaky handheld videosUp to 29 hoursvideo playback4A16 Bionic chipFace IDNewiPhone 14A total powerhouse.***BuyLearn moreViewiPhone 14in AR6.7 or 6.1Super Retina XDRdisplay6Emergency SOSvia satellite2Emergency SOSCrash DetectionAdvanceddual-camera system12MP MainUltra WidePhotonic Engine for incredible detail and colorAutofocuson TrueDepthfront cameraAction mode smooths out shaky handheld videosUp to 26 hoursvideo playback4A15 Bionic chipwith 5-core GPUFace IDiPhone 13As amazing as ever.***BuyLearn moreViewiPhone 13 and iPhone 13 miniin AR6.1 or 5.4Super Retina XDRdisplay6Emergency SOSDualcamera system12MP MainUltra WideTrueDepthfront cameraUp to 19 hoursvideo playback4A15 Bionic chipwith 4-core GPUFace IDiPhone SESerious power. Serious value.BuyLearn moreViewiPhone SEin AR4.7Retina HDdisplayEmergency SOSAdvanced camera system12MP MainFront cameraUp to 15 hoursvideo playback4A15 Bionic chipwith 4-core GPUTouch IDCompare all iPhone modelsShop iPhoneApple FooterFast, free deliveryOr pick up available items at an Apple Store.Learn morePay monthly at 0% APRYou can pay over time when you choose to check out with Apple Card Monthly Installments.Learn moreGet help buyingHave a question? Call a Specialist or chat online.Call 1-800-MY-APPLE.Contact us*Trade-in values will vary based on the condition, year, and configuration of your eligible tradein device. Not all devices are eligible for credit. You must be at least 18 years old to be eligible to trade in for credit or for an Apple Gift Card. Tradein value may be applied toward qualifying new device purchase, or added to an Apple Gift Card. Actual value awarded is based on receipt of a qualifying device matching the description provided when estimate was made. Sales tax may be assessed on full value of a new device purchase. Instore tradein requires presentation of a valid photo ID (local law may require saving this information). Offer may not be available in all stores, and may vary between instore and online tradein. Some stores may have additional requirements. Apple or its tradein partners reserve the right to refuse or limit quantity of any tradein transaction for any reason. More details are available from Apples tradein partner for tradein and recycling of eligible devices. Restrictions and limitations may apply.**Pricing for iPhone 14 and iPhone 14 Plus includes a $30 connectivity discount that requires activation with AT&T, T-Mobile, Sprint, or Verizon. Available to qualified customers and requires 24month installment loan when you select Citizens One or Apple Card Monthly Installments (ACMI) as payment type at checkout at Apple. iPhone activation required with AT&T, T-Mobile, Sprint, or Verizon for purchases made with ACMI at an Apple Store. Subject to credit approval and credit limit. Taxes and shipping are not included in ACMI and are subject to your cards variable APR. Additional Apple Card Monthly Installments terms are in the Apple Card Customer Agreement. Additional iPhone Payments terms arehere. ACMI is not available for purchases made online at special storefronts. The last months payment for each product will be the products purchase price, less all other payments at the monthly payment amount.***Pricing includes a $30 connectivity discount that requires activation with AT&T, TMobile, Sprint, or Verizon.iPhone 14 and iPhone 14 Plus are splash, water, and dust resistant and were tested under controlled laboratory conditions with a rating of IP68 under IEC standard 60529 (maximum depth of 6 meters up to 30 minutes). Splash, water, and dust resistance are not permanent conditions. Resistance might decrease as a result of normal wear. Do not attempt to charge a wet iPhone; refer to the user guide for cleaning and drying instructions. Liquid damage not covered under warranty.Service is included for free for two years with the activation of any iPhone 14 model. Connection and response times vary based on location, site conditions, and other factors. Seehttps://support.apple.com/kb/HT213426for more information.Emergency SOS uses a cellular connection or WiFi Calling.All battery claims depend on network configuration and many other factors; actual results will vary. Battery has limited recharge cycles and may eventually need to be replaced. Battery life and charge cycles vary by use and settings. Seeapple.com/batteriesandapple.com/iphone/battery.htmlfor more information.Accessories sold separately.The display has rounded corners that follow a beautiful curved design, and these corners are within a standard rectangle. When measured as a standard rectangular shape, the screen is 5.42 inches (iPhone 13 mini, iPhone 12 mini), 5.85 inches (iPhone 11 Pro, iPhone XS, iPhone X), 6.06 inches (iPhone 14, iPhone 13 Pro, iPhone 13, iPhone 12 Pro, iPhone 12, iPhone 11, iPhone XR), 6.12 inches (iPhone 14 Pro), 6.46 inches (iPhone 11 Pro Max, iPhone XS Max), 6.68 inches (iPhone 14 Plus, iPhone 13 Pro Max, iPhone 12 Pro Max), or 6.69 inches (iPhone 14 Pro Max) diagonally. Actual viewable area is less.iPhone 14 models are activated with an eSIM and do not support a physical SIM. Use of an eSIM requires a carrier that supports eSIM and a wireless service plan (which may include restrictions on switching service providers and roaming, even after contract expiration). See your carrier for details. To learn more, visitapple.com/esim.Trade-in values will vary based on the condition, year, and configuration of your eligible tradein device. Not all devices are eligible for credit. You must be at least 18 years old to be eligible to trade in for credit or for an Apple Gift Card. Tradein value may be applied toward qualifying new device purchase, or added to an Apple Gift Card. Actual value awarded is based on receipt of a qualifying device matching the description provided when estimate was made. Sales tax may be assessed on full value of a new device purchase. Instore tradein requires presentation of a valid photo ID (local law may require saving this information). Offer may not be available in all stores, and may vary between instore and online tradein. Some stores may have additional requirements. Apple or its tradein partners reserve the right to refuse or limit quantity of any tradein transaction for any reason. More details are available from Apples tradein partner for tradein and recycling of eligible devices. Restrictions and limitations may apply.Program available for iPhone 14 and iPhone 14 Pro. Available to qualified customers with a credit check and eligible U.S. credit or debit card. Requires a 24month installment loan with a 0% APR from Citizens Bank, N.A. (subject to any interest, fees, or other costs payable to the card issuer), purchase of AppleCare+ for iPhone, and iPhone activation with one of these national carriers: AT&T, Sprint, Verizon, or TMobile. Sales tax and any applicable fees due at time of purchase. Full terms apply.AT&T Special Deal:Monthly price reflects net monthly payment, after application of AT&T tradein credit applied over 36 months with purchase of an iPhone 14 Pro, iPhone 14 Pro Max, iPhone 14, or iPhone 14 Plus and tradein of eligible smartphone. Receive credit with purchase of an iPhone 14, iPhone 14 Plus, iPhone 14 Pro, or iPhone 14 Pro Max of either $800, or $350 (based upon the model and condition of your tradein smartphone), max bill credits will not exceed the cost of the device. Requires upgrade of an existing line or activation of a new line and purchase of a new iPhone 14, iPhone 14 Plus, iPhone 14 Pro, or iPhone 14 Pro Max on qualifying 36 month 0% APR installment plan, subject to carrier credit qualification. AT&T Installment Plan with Next Up is not eligible for this promotion. $0 down for well qualified customers only, or down payment may be required and depends on a variety of factors. Tax on full retail price due at sale. Requires activation on eligible unlimited plan. If you cancel eligible wireless service, credits will stop and you will owe the remaining device balance. Activation/Upgrade Fee: $35. Trade in device may not be on existing installment plan. Bill credits are applied as a monthly credit over the 36 month installment plan. Credits start within 3 bills. Will receive catchup credits once credits start. Wireless line must be on an installment agreement, active, and in good standing for 30 days to qualify. Installment agreement starts when device is shipped. To get all credits, device must remain on agreement for entire term and you must keep eligible service on device for entire installment term. Limited time offer; subject to change. Limits: one tradein per qualifying purchase and one credit per line. May not be combinable with other offers, discounts, or credits. Purchase, financing, other limits, and restrictions apply. Price for iPhone 14 and iPhone 14 Plus includes $30 AT&T connectivity discount. Activation required.Sprint Special Deal:Sprint tradein credit in the form of a rebate with virtual prepaid card when you trade in a qualifying device. Limited-time offer; subject to change. Requires activation on any Sprint data plan and submission of a promo code atpromotions.t-mobile.com. $200 rebate via virtual prepaid Mastercard Card, which you can use online or instore via accepted mobile payment apps; no cash access & expires in 6 months from issuance. Card is issued by Sunrise Banks N.A., Member FDIC, pursuant to a license from Mastercard International Incorporated. Mastercard is a registered trademark of Mastercard International Incorporated. Use of this card constitutes acceptance of the terms and conditions stated in the Cardholder Agreement. Lines must be active and in good standing when card is issued. Allow up to 2 billing cycles after fulfillment of offer requirements. Max 4 per account offer/discounted devices/account. May not be combined with some offers or discounts. Sales tax may be assessed on full value of new iPhone. Requires tradein of an iPhone XRor newer in good condition, including iPhone SE (2nd generation). Must be at least 18 to trade in. Apple or its tradein partners reserve the right to refuse or limit any tradein transaction for any reason. Instore tradein requires presentation of a valid, government-issued photo ID (local law may require saving this information). Instore promotion availability subject to local law; speak to a Specialist to learn more. Additional terms from Apple, Sprint, and Apples tradein partners may apply.TMobile Special Deal:Monthly price reflects net monthly payment, after application of TMobile tradein credit applied over 24 months with purchase of an iPhone 14 Pro, iPhone 14 Pro Max, iPhone 14, or iPhone 14 Plus and tradein of eligible smartphone. Receive credit with purchase of an iPhone 14, iPhone 14 Plus, iPhone 14 Pro, or iPhone 14 Pro Max of $400 or $200 (based upon the model and condition of your tradein smartphone) for customers on any eligible rate plan. Max bill credits will not exceed the cost of the device. Credit comprised of (i) Apple instant tradein credit at checkout and (ii) TMobile monthly bill credits applied over 24 months. Customer must remain in the TMobile Equipment Installment Program and on eligible rate plan for 24 months and remain in good standing to receive the full benefit of the bill credits; allow 2 bill cycles from valid submission and validation of tradein. Tax on precredit price due at sale. Limitedtime offer; subject to change. Qualifying credit, data plan, and tradein in good condition required. Max 4 promotional offers on any iPhone per account. May not be combinable with some offers or discounts. Price for iPhone 14 and iPhone 14 Plus includes $30 TMobile connectivity discount. Activation required.Verizon Special Deal:Monthly price reflects net monthly payment, after application of Verizon tradein credit applied over 36 months with purchase of an iPhone 14 Pro, iPhone 14 Pro Max, iPhone 14, or iPhone 14 Plus with credit of $800 or $400 for customers on a Get More or One Unlimited plan (based upon the model and condition of your tradein smartphone); or $440 or $220 for customers on a Do More or Play More plan (based upon the model and condition of your tradein smartphone). Credit comprised of (i) Apple instant tradein credit at checkout and (ii) Verizon monthly bill credits applied over 36 months. Customer must remain in the Verizon Device Payment Program for 36 months to receive the full benefit of the Verizon bill credits. Bill credits may take 12 bill cycles to appear. If it takes two cycles for bill credits to appear, youll see the credit for the first cycle on your second bill in addition to that months credit. Requires purchase and activation of a new iPhone 14, iPhone 14 Plus, iPhone 14 Pro, or iPhone 14 Pro Max with the Verizon Device Payment Program at 0% APR for 36 months, subject to carrier credit qualification, and iPhone availability and limits. Taxes and shipping not included in monthly price. Sales tax may be assessed on full value of new iPhone. Requires eligible unlimited service plan. Requires tradein of eligible device in eligible condition. Must be at least 18 to tradein. Apple or its tradein partners reserve the right to refuse or limit any tradein transaction for any reason. Instore tradein requires presentation of a valid, governmentissued photo ID (local law may require saving this information). Instore promotion availability subject to local law; speak to a Specialist to learn more. Limitedtime offer; subject to change. Additional terms from Apple, Verizon, and Apples tradein partners may apply. Price for iPhone 14 and iPhone 14 Plus includes $30 Verizon connectivity discount. Activation required.Apple Fitness+ requires an iPhone 8 or later with iOS 16.1.Some features may not be available for all countries or all areas.View complete list.Apple Card Monthly Installments (ACMI) is a 0% APR payment option available only in the U.S. to select at checkout for certain Apple products purchased at Apple Store locations,apple.com, the Apple Store app, or by calling 1-800-MY-APPLE and is subject to credit approval and credit limit. Seesupport.apple.com/kb/HT211204for more information about eligible products. Variable APRs for Apple Card other than ACMI range from 15.24% to 26.24% based on creditworthiness. Rates as of January 1, 2023.If you choose the payinfull or onetimepayment option for an ACMIeligible purchase instead of choosing ACMI as the payment option at checkout, that purchase will be subject to the variable APR assigned to your Apple Card. Taxes and shipping are not included in ACMI and are subject to your cards variable APR. See theApple Card Customer Agreementfor more information. ACMI is not available for purchases made online at the following special stores: Apple Employee Purchase Plan; participating corporate Employee Purchase Programs; Apple at Work for small businesses; Government, and Veterans and Military Purchase Programs, or on refurbished devices. iPhone activation required on iPhone purchases made at an Apple Store with one of these national carriers: AT&T, Sprint, Verizon, or TMobile.To access and use all the features of Apple Card, you must add Apple Card to Wallet on an iPhone or iPad with the latest version of iOS or iPadOS. Update to the latest version by going to Settings > General > Software Update. Tap Download and Install.Available for qualifying applicants in the United States.Apple Card is issued by Goldman Sachs Bank USA, Salt Lake City Branch.AppleiPhoneiPhone 14Shop and LearnShop and Learn+StoreMaciPadiPhoneWatchAirPodsTV & HomeAirTagAccessoriesGift CardsApple WalletApple Wallet+WalletApple CardApple PayApple CashAccountAccount+Manage Your Apple IDApple Store AccountiCloud.comEntertainmentEntertainment+Apple OneApple TV+Apple MusicApple ArcadeApple Fitness+Apple News+Apple PodcastsApple BooksApp StoreApple StoreApple Store+Find a StoreGenius BarToday at AppleApple CampApple Store AppCertified RefurbishedFinancingApple Trade InOrder StatusShopping HelpFor BusinessFor Business+Apple and BusinessShop for BusinessFor EducationFor Education+Apple and EducationShop for K-12Shop for CollegeFor HealthcareFor Healthcare+Apple in HealthcareHealth on Apple WatchHealth Records on iPhoneFor GovernmentFor Government+Shop for GovernmentShop for Veterans and MilitaryApple ValuesApple Values+AccessibilityEducationEnvironmentInclusion and DiversityPrivacyRacial Equity and JusticeSupplier ResponsibilityAbout AppleAbout Apple+NewsroomApple LeadershipCareer OpportunitiesInvestorsEthics & ComplianceEventsContact AppleMore ways to shop:Find an Apple Storeorother retailernear you.Or call 1-800-MY-APPLE.United StatesCopyright 2023 Apple Inc. All rights reserved.Privacy PolicyTerms of UseSales and RefundsLegalSite Map'
    return text



def main():
    text = example()
    tokenized = tokenize(text)
    print(type(tokenized))


if __name__ == '__main__':
    main()


