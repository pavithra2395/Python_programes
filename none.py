<!DOCTYPE html>
<!-- saved from url=(0100)https://stackoverflow.com/questions/48301186/cropping-concave-polygon-from-image-using-opencv-python -->
<html itemscope="" itemtype="http://schema.org/QAPage" class="html__responsive"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">

        <title>Cropping Concave polygon from Image using Opencv python - Stack Overflow</title>
        <link rel="shortcut icon" href="https://cdn.sstatic.net/Sites/stackoverflow/Img/favicon.ico?v=ec617d715196">
        <link rel="apple-touch-icon" href="https://cdn.sstatic.net/Sites/stackoverflow/Img/apple-touch-icon.png?v=c78bd457575a">
        <link rel="image_src" href="https://cdn.sstatic.net/Sites/stackoverflow/Img/apple-touch-icon.png?v=c78bd457575a"> 
        <link rel="search" type="application/opensearchdescription+xml" title="Stack Overflow" href="https://stackoverflow.com/opensearch.xml">
        <link rel="canonical" href="https://stackoverflow.com/questions/48301186/cropping-concave-polygon-from-image-using-opencv-python">
        <meta name="viewport" content="width=device-width, height=device-height, initial-scale=1.0, minimum-scale=1.0">
        <meta property="og:type" content="website">
        <meta property="og:url" content="https://stackoverflow.com/questions/48301186/cropping-concave-polygon-from-image-using-opencv-python">
        <meta property="og:site_name" content="Stack Overflow">
        <meta property="og:image" itemprop="image primaryImageOfPage" content="https://cdn.sstatic.net/Sites/stackoverflow/Img/apple-touch-icon@2.png?v=73d79a89bded">
        <meta name="twitter:card" content="summary">
        <meta name="twitter:domain" content="stackoverflow.com">
        <meta name="twitter:title" property="og:title" itemprop="name" content="Cropping Concave polygon from Image using Opencv python">
        <meta name="twitter:description" property="og:description" itemprop="description" content="How can I crop a concave polygon from an image. My Input image look like 
.

and the coordinates of closed polygon are 
[10,150],[150,100],[300,150],[350,100],[310,20],[35,10]. I want region bounde...">

        <script src="./none_files/osd.js.download"></script><script src="./none_files/amp4ads-host-v0.js.download"></script><script src="./none_files/rules-p-c1rF4kxgLUzNc.js.download" async=""></script><script async="" src="./none_files/quant.js.download"></script><script async="" src="./none_files/beacon.js.download"></script><script async="" src="./none_files/analytics.js.download"></script><script src="./none_files/jquery.min.js.download"></script>
        <script src="./none_files/stub.en.js.download"></script>
    
        <link rel="stylesheet" type="text/css" href="./none_files/stacks.css">
        <link rel="stylesheet" type="text/css" href="./none_files/primary.css">

    
            <link rel="alternate" type="application/atom+xml" title="Feed for question &#39;Cropping Concave polygon from Image using Opencv python&#39;" href="https://stackoverflow.com/feeds/question/48301186">
            <meta name="twitter:app:country" content="US">
            <meta name="twitter:app:name:iphone" content="Stack Exchange iOS">
            <meta name="twitter:app:id:iphone" content="871299723">
            <meta name="twitter:app:url:iphone" content="se-zaphod://stackoverflow.com/questions/48301186/cropping-concave-polygon-from-image-using-opencv-python">
            <meta name="twitter:app:name:ipad" content="Stack Exchange iOS">
            <meta name="twitter:app:id:ipad" content="871299723">
            <meta name="twitter:app:url:ipad" content="se-zaphod://stackoverflow.com/questions/48301186/cropping-concave-polygon-from-image-using-opencv-python">
            <meta name="twitter:app:name:googleplay" content="Stack Exchange Android">
            <meta name="twitter:app:url:googleplay" content="http://stackoverflow.com/questions/48301186/cropping-concave-polygon-from-image-using-opencv-python">
            <meta name="twitter:app:id:googleplay" content="com.stackexchange.marvin">
        <script>
            StackExchange.ready(function () {

                    StackExchange.using("snippets", function () {
                        StackExchange.snippets.initSnippetRenderer();
                    });
                    
                StackExchange.using("postValidation", function () {
                    StackExchange.postValidation.initOnBlurAndSubmit($('#post-form'), 2, 'answer');
                });


                StackExchange.question.init({showAnswerHelp:true,totalCommentCount:1,shownCommentCount:1,questionId:48301186});

                styleCode();

                    StackExchange.realtime.subscribeToQuestion('1', '48301186');
                    StackExchange.using("gps", function () { StackExchange.gps.trackOutboundClicks('#content', '.js-post-body'); });



            });
        </script>

        
        
        
        
        
        
        


    <script>
        StackExchange.init({"locale":"en","serverTime":1599218326,"routeName":"Questions/Show","stackAuthUrl":"https://stackauth.com","networkMetaHostname":"meta.stackexchange.com","site":{"name":"Stack Overflow","description":"Q&A for professional and enthusiast programmers","isNoticesTabEnabled":true,"enableNewTagCreationWarning":true,"insertSpaceAfterNameTabCompletion":false,"id":1,"childUrl":"https://meta.stackoverflow.com","styleCodeWithHighlightjs":false,"negativeVoteScoreFloor":null,"enableSocialMediaInSharePopup":true,"protocol":"https"},"user":{"fkey":"06f4a5ec10401c8de359874849bfe5f8510ad6928c6d18bc248daae27aa762fb","tid":"eb136534-ed85-37b3-7be1-4760c18eb0c0","rep":0,"isAnonymous":true,"isAnonymousNetworkWide":true},"events":{"postType":{"question":1},"postEditionSection":{"title":1,"body":2,"tags":3}},"story":{"minCompleteBodyLength":75,"likedTagsMaxLength":300,"dislikedTagsMaxLength":300},"jobPreferences":{"maxNumDeveloperRoles":2,"maxNumIndustries":4},"svgIconPath":"https://cdn.sstatic.net/Img/svg-icons","svgIconHash":"e06df390d347"}, {"userProfile":{"openGraphAPIKey":"4a307e43-b625-49bb-af15-ffadf2bda017"},"userMessaging":{"showNewFeatureNotice":true},"tags":{},"subscriptions":{"defaultMaxTrueUpSeats":1000},"snippets":{"renderDomain":"stacksnippets.net","snippetsEnabled":true},"slack":{"sidebarAdDismissCookie":"slack-sidebar-ad","sidebarAdDismissCookieExpirationDays":60.0},"site":{"allowImageUploads":true,"enableImgurHttps":true,"enableUserHovercards":true,"forceHttpsImages":true,"styleCode":true},"paths":{},"monitoring":{"clientTimingsAbsoluteTimeout":30000,"clientTimingsDebounceTimeout":1000},"mentions":{"maxNumUsersInDropdown":50},"markdown":{"asteriskIntraWordEmphasis":true,"enableCommonmark":true},"flags":{"allowRetractingCommentFlags":true,"allowRetractingFlags":true},"comments":{},"accounts":{"currentPasswordRequiredForChangingStackIdPassword":true}});
        StackExchange.using.setCacheBreakers({"js/adops.en.js":"22a9bd59b1e9","js/ask.en.js":"f4270fa633d7","js/begin-edit-event.en.js":"410e2aaf036a","js/events.en.js":"397938b4f0dd","js/explore-qlist.en.js":"5da8ae80881e","js/full-anon.en.js":"9bdf567f774c","js/full.en.js":"6668347ca2d1","js/help.en.js":"76e2886f2122","js/highlightjs-loader.en.js":"19b4c61638f5","js/inline-tag-editing.en.js":"1b88a7bb274f","js/keyboard-shortcuts.en.js":"4402866018c0","js/mobile.en.js":"c9a1442de96b","js/moderator.en.js":"2565e0ff5cd4","js/postCollections-transpiled.en.js":"75c164461bf7","js/post-validation.en.js":"57139e856906","js/prettify-full.en.js":"5c8f593b8aa5","js/question-editor.en.js":"","js/review.en.js":"540f949258ec","js/revisions.en.js":"acbd0c518df5","js/tageditor.en.js":"8b49dad16a3b","js/tageditornew.en.js":"966a75127fbf","js/tagsuggestions.en.js":"9b2c5d9791d2","js/third-party/stacks-editor/app.bundle.js":"3ae7ceece3e2","js/third-party/stacks-editor/app.bundle.en.js":"","js/wmd.en.js":"25f97e81fc9c","js/snippet-javascript-codemirror.en.js":"6224800d8f71","js/markdown-it-loader.en.js":"1eed517683e1"});
        StackExchange.using("gps", function() {
             StackExchange.gps.init(true);
        });
    </script>
    <noscript id="noscript-css"><style>body,.top-bar{margin-top:1.9em}</style></noscript>
    <script async="" src="./none_files/full-anon.en.js.download"></script><script src="./none_files/pubads_impl_2020083101.js.download" async=""></script><link rel="stylesheet" href="./none_files/clc.min.css" type="text/css"><script async="" src="./none_files/post-validation.en.js.download"></script><script async="" src="./none_files/prettify-full.en.js.download"></script><link rel="preload" href="./none_files/f.txt" as="script"><script type="text/javascript" src="./none_files/f.txt"></script><link rel="preload" href="./none_files/f(1).txt" as="script"><script type="text/javascript" src="./none_files/f(1).txt"></script><link rel="prefetch" href="https://403e2a47138c8ed5c8dcb84e240852f1.safeframe.googlesyndication.com/safeframe/1-0-37/html/container.html"><link rel="prefetch" href="https://tpc.googlesyndication.com/safeframe/1-0-37/html/container.html"></head>
    <body class="question-page unified-theme">
    <div id="notify-container"></div>
    <div id="custom-header"></div>
        
<header class="top-bar js-top-bar top-bar__network _fixed">
    <div class="wmx12 mx-auto grid ai-center h100" role="menubar">
        <div class="-main grid--cell">
                <a href="https://stackoverflow.com/questions/48301186/cropping-concave-polygon-from-image-using-opencv-python#" class="left-sidebar-toggle p0 ai-center jc-center js-left-sidebar-toggle" role="menuitem" aria-haspopup="true" aria-controls="left-sidebar" aria-expanded="false"><span class="ps-relative"></span></a>
                <div class="topbar-dialog leftnav-dialog js-leftnav-dialog dno">
                    <div class="left-sidebar js-unpinned-left-sidebar" data-can-be="left-sidebar" data-is-here-when="sm"></div>
                </div>
                    <a href="https://stackoverflow.com/" class="-logo js-gps-track" data-gps-track="top_nav.click({is_current:false, location:2, destination:8})">
                        <span class="-img _glyph">Stack Overflow</span>
                    </a>



        </div>

            <ol class="list-reset grid gs4" role="presentation">

                    <li class="grid--cell md:d-none">
                        <a href="https://stackoverflow.com/company" class="-marketing-link js-gps-track" data-gps-track="top_nav.products.click({location:2, destination:7})" data-ga="[&quot;top navigation&quot;,&quot;about menu click&quot;,null,null,null]">About</a>
                    </li>

                <li class="grid--cell">
                    <a href="https://stackoverflow.com/questions/48301186/cropping-concave-polygon-from-image-using-opencv-python#" class="-marketing-link js-gps-track js-products-menu" aria-controls="products-popover" data-controller="s-popover" data-action="s-popover#toggle" data-s-popover-placement="bottom" data-s-popover-toggle-class="is-selected" data-gps-track="top_nav.products.click({location:2, destination:1})" data-ga="[&quot;top navigation&quot;,&quot;products menu click&quot;,null,null,null]">
                        Products
                    </a>
                </li>

                    <li class="grid--cell md:d-none">
                        <a href="https://stackoverflow.com/teams" class="-marketing-link js-gps-track" data-gps-track="top_nav.products.click({location:2, destination:7})" data-ga="[&quot;top navigation&quot;,&quot;learn more - teams&quot;,null,null,null]">For Teams</a>
                    </li>
            </ol>
            <div class="s-popover ws2 mtn2 p0" id="products-popover" role="menu" aria-hidden="true">
                <div class="s-popover--arrow"></div>
                <ol class="list-reset s-anchors s-anchors__inherit">
                    <li class="m6">
                        <a href="https://stackoverflow.com/questions" class="bar-sm p6 d-block h:bg-black-100 js-gps-track" data-gps-track="top_nav.products.click({location:2, destination:2})" data-ga="[&quot;top navigation&quot;,&quot;public qa submenu click&quot;,null,null,null]">
                            <span class="fs-body1 d-block">Stack Overflow</span>
                            <span class="fs-caption d-block fc-light">Public questions &amp; answers</span>
                        </a>
                    </li>
                    <li class="m6">
                        <a href="https://stackoverflow.com/teams" class="bar-sm p6 d-block h:bg-black-100 js-gps-track" data-gps-track="top_nav.products.click({location:2, destination:3})" data-ga="[&quot;top navigation&quot;,&quot;teams submenu click&quot;,null,null,null]">
                            <span class="fs-body1 d-block">Stack Overflow for Teams</span>
                            <span class="fs-caption d-block fc-light">Where developers &amp; technologists share private knowledge with coworkers</span>
                        </a>
                    </li>
                    <li class="m6">
                        <a href="https://stackoverflow.com/jobs?so_source=ProductsMenu&amp;so_medium=StackOverflow" class="bar-sm p6 d-block h:bg-black-100 js-gps-track" data-gps-track="top_nav.products.click({location:2, destination:9})" data-ga="[&quot;top navigation&quot;,&quot;jobs submenu click&quot;,null,null,null]">
                            <span class="fs-body1 d-block">Jobs</span>
                            <span class="fs-caption d-block fc-light">Programming &amp; related technical career opportunities</span>
                        </a>
                    </li>
                    <li class="m6">
                        <a href="https://stackoverflow.com/talent" class="bar-sm p6 d-block h:bg-black-100 js-gps-track" data-gps-track="top_nav.products.click({location:2, destination:5})" data-ga="[&quot;top navigation&quot;,&quot;talent submenu click&quot;,null,null,null]">
                            <span class="fs-body1 d-block">Talent</span>
                            <span class="fs-caption d-block fc-light">Recruit tech talent &amp; build your employer brand</span>
                        </a>
                    </li>
                    <li class="m6">
                        <a href="https://stackoverflow.com/advertising" class="bar-sm p6 d-block h:bg-black-100 js-gps-track" data-gps-track="top_nav.products.click({location:2, destination:6})" data-ga="[&quot;top navigation&quot;,&quot;advertising submenu click&quot;,null,null,null]">
                            <span class="fs-body1 d-block">Advertising</span>
                            <span class="fs-caption d-block fc-light">Reach developers &amp; technologists worldwide</span>
                        </a>
                    </li>
                    <li class="bg-black-025 bt bc-black-2 py6 px6 bbr-sm">
                        <a href="https://stackoverflow.com/company" class="fc-light d-block py6 px6 h:fc-black-800 js-gps-track" data-gps-track="top_nav.products.click({location:2, destination:7})" data-ga="[&quot;top navigation&quot;,&quot;about submenu click&quot;,null,null,null]">About the company</a>
                    </li>
                </ol>
            </div>

            <form id="search" role="search" action="https://stackoverflow.com/search" method="get" class="grid--cell fl-grow1 searchbar px12 js-searchbar " autocomplete="off">
                    <div class="ps-relative">
                        <input name="q" type="text" placeholder="Search…" value="" autocomplete="off" maxlength="240" class="s-input s-input__search js-search-field " aria-label="Search" aria-controls="top-search" data-controller="s-popover" data-action="focus-&gt;s-popover#show" data-s-popover-placement="bottom-start">
                        <svg aria-hidden="true" class="s-input-icon s-input-icon__search svg-icon iconSearch" width="18" height="18" viewBox="0 0 18 18"><path d="M18 16.5l-5.14-5.18h-.35a7 7 0 10-1.19 1.19v.35L16.5 18l1.5-1.5zM12 7A5 5 0 112 7a5 5 0 0110 0z"></path></svg>
                        <div class="s-popover p0 wmx100 wmn4 sm:wmn-initial js-top-search-popover s-popover--arrow__tl" id="top-search" role="menu">
    <div class="js-spinner p24 grid ai-center jc-center d-none">
        <div class="s-spinner s-spinner__sm fc-orange-400">
            <div class="v-visible-sr">Loading…</div>
        </div>
    </div>

    <span class="v-visible-sr js-screen-reader-info"></span>
    <div class="js-ac-results overflow-y-auto hmx3 d-none"></div>

    <div class="js-search-hints" aria-describedby="Tips for searching"></div>
</div>
                    </div>
            </form>
        
        

<ol class="overflow-x-auto ml-auto -secondary grid ai-center list-reset h100 user-logged-out" role="presentation">
        <li class="-item searchbar-trigger"><a href="https://stackoverflow.com/questions/48301186/cropping-concave-polygon-from-image-using-opencv-python#" class="-link js-searchbar-trigger" role="button" aria-label="Search" aria-haspopup="true" aria-controls="search" title="Click to show search"><svg aria-hidden="true" class="svg-icon iconSearch" width="18" height="18" viewBox="0 0 18 18"><path d="M18 16.5l-5.14-5.18h-.35a7 7 0 10-1.19 1.19v.35L16.5 18l1.5-1.5zM12 7A5 5 0 112 7a5 5 0 0110 0z"></path></svg></a></li>

            <li class="-ctas">
                            <a href="https://stackoverflow.com/users/login?ssrc=head&amp;returnurl=https%3a%2f%2fstackoverflow.com%2fquestions%2f48301186%2fcropping-concave-polygon-from-image-using-opencv-python" class="login-link s-btn s-btn__filled py8 js-gps-track" rel="nofollow" data-gps-track="login.click" data-ga="[&quot;top navigation&quot;,&quot;login button click&quot;,null,null,null]">Log in</a>
                            <a href="https://stackoverflow.com/users/signup?ssrc=head&amp;returnurl=%2fusers%2fstory%2fcurrent" class="login-link s-btn s-btn__primary py8" rel="nofollow" data-ga="[&quot;sign up&quot;,&quot;Sign Up Navigation&quot;,&quot;Header&quot;,null,null]">Sign up</a>

            </li>

    <li class="js-topbar-dialog-corral" role="presentation">
            

    <div class="topbar-dialog siteSwitcher-dialog dno" role="menu">
        <div class="header">
            <h3>
                <a href="https://stackoverflow.com/">current community</a>
            </h3>
        </div>
        <div class="modal-content bg-powder-050">
            <ul class="current-site">
                    <li class="grid">
                            <div class="fl1">
                <a href="https://stackoverflow.com/" class="current-site-link site-link js-gps-track grid gs8 gsx" data-id="1" data-gps-track="site_switcher.click({ item_type:3 })">
        <div class="favicon favicon-stackoverflow site-icon grid--cell" title="Stack Overflow"></div>
        <span class="grid--cell fl1">
            Stack Overflow
        </span>
    </a>

    </div>
    <div class="related-links">
            <a href="https://stackoverflow.com/help" class="js-gps-track" data-gps-track="site_switcher.click({ item_type:14 })">help</a>
            <a href="https://chat.stackoverflow.com/" class="js-gps-track" data-gps-track="site_switcher.click({ item_type:6 })">chat</a>
    </div>

                    </li>
                    <li class="related-site grid">
                            <div class="L-shaped-icon-container">
        <span class="L-shaped-icon"></span>
    </div>

                            <a href="https://meta.stackoverflow.com/" class=" site-link js-gps-track grid gs8 gsx" data-id="552" data-gps-track="site.switch({ target_site:552, item_type:3 }),site_switcher.click({ item_type:4 })">
        <div class="favicon favicon-stackoverflowmeta site-icon grid--cell" title="Meta Stack Overflow"></div>
        <span class="grid--cell fl1">
            Meta Stack Overflow
        </span>
    </a>

                    </li>
            </ul>
        </div>

        <div class="header" id="your-communities-header">
            <h3>
your communities            </h3>

        </div>
        <div class="modal-content" id="your-communities-section">

                <div class="call-to-login">
<a href="https://stackoverflow.com/users/signup?ssrc=site_switcher&amp;returnurl=%2fusers%2fstory%2fcurrent" class="login-link js-gps-track" data-gps-track="site_switcher.click({ item_type:10 })">Sign up</a> or <a href="https://stackoverflow.com/users/login?ssrc=site_switcher&amp;returnurl=https%3a%2f%2fstackoverflow.com%2fquestions%2f48301186%2fcropping-concave-polygon-from-image-using-opencv-python" class="login-link js-gps-track" data-gps-track="site_switcher.click({ item_type:11 })">log in</a> to customize your list.                </div>
        </div>

        <div class="header">
            <h3><a href="https://stackexchange.com/sites">more stack exchange communities</a>
            </h3>
            <a href="https://stackoverflow.blog/" class="fr">company blog</a>
        </div>
        <div class="modal-content">
                <div class="child-content"></div>
        </div>        
    </div>

    </li>
</ol>
    </div>
</header>
    <div id="js-gdpr-consent-banner" class="p8 ff-sans ps-fixed b0 l0 r0 z-banner" role="banner" aria-hidden="false" style="background-color: #3b4045; color: white;"> 
        <div class="wmx8 mx-auto grid grid__center" role="alertdialog" aria-describedby="notice-message">
            <div class="grid--cell mr12" aria-label="notice-message">
                <p class="mb0 lh-lg">
                    By using our site, you acknowledge that you have read and understand our <a class="s-link s-link__inherit td-underline fc-white" target="_blank" href="https://stackoverflow.com/legal/cookie-policy">Cookie Policy</a>, <a class="s-link s-link__inherit td-underline fc-white" target="_blank" href="https://stackoverflow.com/legal/privacy-policy">Privacy Policy</a>, and our <a class="s-link s-link__inherit td-underline fc-white" target="_blank" href="https://stackoverflow.com/legal/terms-of-service/public">Terms of Service</a>.
                </p>
            </div>
            <div class="grid--cell">
                <a class="s-btn s-btn__muted s-btn__icon js-notice-close" aria-label="notice-dismiss">
                    <svg aria-hidden="true" class="svg-icon iconClear" width="18" height="18" viewBox="0 0 18 18"><path d="M15 4.41L13.59 3 9 7.59 4.41 3 3 4.41 7.59 9 3 13.59 4.41 15 9 10.41 13.59 15 15 13.59 10.41 9 15 4.41z"></path></svg>
                </a>
            </div>
        </div>
    </div>

    <script>
        StackExchange.ready(function () { StackExchange.topbar.init(); });
StackExchange.scrollPadding.setPaddingTop(50, 10);    </script>





    <div class="container">
            


<div id="left-sidebar" data-is-here-when="md lg" class="left-sidebar js-pinned-left-sidebar ps-relative">
    <div class="left-sidebar--sticky-container js-sticky-leftnav">
        <nav role="navigation">
            <ol class="nav-links">
        <li class="">
            <a href="https://stackoverflow.com/" class="pl8 js-gps-track nav-links--link" data-gps-track="top_nav.click({is_current:false, location:2, destination:8})">
Home            </a>
        </li>
                <li>
                    <ol class="nav-links">
                            <li class="fs-fine tt-uppercase ml8 mt16 mb4 fc-light">Public</li>
                                <li class=" youarehere">
            <a id="nav-questions" href="https://stackoverflow.com/questions" class="pl8 js-gps-track nav-links--link -link__with-icon" data-gps-track="top_nav.click({is_current:true, location:2, destination:1})">
<svg aria-hidden="true" class="svg-icon iconGlobe" width="18" height="18" viewBox="0 0 18 18"><path d="M9 1a8 8 0 100 16A8 8 0 009 1zM8 15.32a6.4 6.4 0 01-5.23-7.75L7 11.68v.8c0 .88.12 1.32 1 1.32v1.52zm5.72-2c-.2-.66-1-1.32-1.72-1.32h-1v-2c0-.44-.56-1-1-1H6V7h1c.44 0 1-.56 1-1V5h2c.88 0 1.4-.72 1.4-1.6v-.33a6.4 6.4 0 012.32 10.24v.01z"></path></svg>                    <span class="-link--channel-name">Stack Overflow</span>
            </a>
        </li>

        <li class="">
            <a id="nav-tags" href="https://stackoverflow.com/tags" class=" js-gps-track nav-links--link" data-gps-track="top_nav.click({is_current:false, location:2, destination:2})">
Tags            </a>
        </li>
        <li class="">
            <a id="nav-users" href="https://stackoverflow.com/users" class=" js-gps-track nav-links--link" data-gps-track="top_nav.click({is_current:false, location:2, destination:3})">
Users            </a>
        </li>
                            <li class="fs-fine tt-uppercase ml8 mt16 mb4 fc-light">Find a Job</li>
        <li class="">
            <a id="nav-jobs" href="https://stackoverflow.com/jobs?so_medium=StackOverflow&amp;so_source=SiteNav" class=" js-gps-track nav-links--link" data-gps-track="top_nav.click({is_current:false, location:2, destination:6})">
Jobs            </a>
        </li>
        <li class="">
            <a id="nav-companies" href="https://stackoverflow.com/jobs/companies?so_medium=StackOverflow&amp;so_source=SiteNav" class=" js-gps-track nav-links--link" data-gps-track="top_nav.click({is_current:false, location:2, destination:12})">
Companies            </a>
        </li>
                    </ol>
                </li>
                    <li>
                        <ol class="nav-links">
                                <li class="grid ai-center jc-space-between ml8 mt24 mb4">
                                    <div class="grid--cell tt-uppercase fs-fine fc-light">Teams</div>
                                    <div class="grid--cell fs-fine fc-light mr4">
                                        <a href="javascript:void(0)" class="s-link s-link__inherit js-gps-track" role="button" aria-controls="popover-teams-create-cta" data-controller="s-popover" data-action="s-popover#toggle" data-s-popover-placement="bottom-start" data-s-popover-toggle-class="is-selected" data-gps-track="teams.create.left-sidenav.click({ Action: ShowInfo })" data-ga="[&quot;teams left navigation - anonymous&quot;,&quot;left nav show teams info&quot;,null,null,null]">
                                            What’s this?
                                        </a>

                                    </div>
                                </li>
                                <li class="ps-relative">
                                    <a href="https://stackoverflow.com/teams" class="pl8 js-gps-track nav-links--link" title="Stack Overflow for Teams is a private, secure spot for your organization&#39;s questions and answers." data-gps-track="teams.create.left-sidenav.click({ Action: TeamsClick })" data-ga="[&quot;teams left navigation - anonymous&quot;,&quot;left nav team click&quot;,&quot;stackoverflow.com/teams&quot;,null,null]">
                                        <div class="grid ai-center">
                                            <div class="grid--cell s-avatar va-middle bg-orange-400">
                                                <div class="s-avatar--letter mtn1">
                                                    <svg aria-hidden="true" class="svg-icon iconBriefcaseSm" width="14" height="14" viewBox="0 0 14 14"><path d="M4 3a1 1 0 011-1h4a1 1 0 011 1v1h.5c.83 0 1.5.67 1.5 1.5v5c0 .83-.67 1.5-1.5 1.5h-7A1.5 1.5 0 012 10.5v-5C2 4.67 2.67 4 3.5 4H4V3zm5 1V3H5v1h4z"></path></svg>
                                                </div>
                                                <svg aria-hidden="true" class="native s-avatar--badge svg-icon iconShieldXSm" width="9" height="10" viewBox="0 0 9 10"><path d="M0 1.84L4.5 0 9 1.84v3.17C9 7.53 6.3 10 4.5 10 2.7 10 0 7.53 0 5.01V1.84z" fill="var(--white)"></path><path d="M1 2.5L4.5 1 8 2.5v2.51C8 7.34 5.34 9 4.5 9 3.65 9 1 7.34 1 5.01V2.5zm2.98 3.02L3.2 7h2.6l-.78-1.48a.4.4 0 01.15-.38c.34-.24.73-.7.73-1.14 0-.71-.5-1.23-1.41-1.23-.92 0-1.39.52-1.39 1.23 0 .44.4.9.73 1.14.12.08.18.23.15.38z" fill="var(--black-500)"></path></svg>
                                            </div>
                                            <div class="grid--cell pl6">
Free 30 Day Trial                                            </div>
                                        </div>
                                    </a>
                                </li>
                        </ol>
                    </li>
            </ol>
        </nav>
    </div>


        <div class="s-popover w-auto p16" id="popover-teams-create-cta" role="menu" aria-hidden="true">
            <div class="s-popover--arrow"></div>

            <div class="ps-relative overflow-hidden">
                <p class="mb2"><strong>Teams</strong></p>
                <p class="mb16 fs-caption fc-medium">Q&amp;A for Work</p>
                <p class="mb8 fs-caption fc-medium">

                            Stack Overflow for Teams is a private, secure spot for you and
                            your coworkers to find and share information.
                                        </p>
                <a href="https://stackoverflow.com/teams" class="js-gps-track ws-nowrap d-block" data-gps-track="teams.create.left-sidenav.click({ Action: CtaClick })" data-ga="[&quot;teams left navigation - anonymous&quot;,&quot;left nav cta&quot;,&quot;stackoverflow.com/teams&quot;,null,null]">
Learn more                </a>
            </div>

            <div class="ps-absolute t8 r8">
                <svg width="53" height="49" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M49 11l.2 31H18.9L9 49v-7H4V8h31" fill="#CCEAFF"></path><path d="M44.5 19v-.3l-.2-.1-18-13-.1-.1H.5v33h4V46l.8-.6 9.9-6.9h29.3V19z" stroke="#1060E1" stroke-miterlimit="10"></path><path d="M31 2l6-1.5 7 2V38H14.9L5 45v-7H1V6h25l5-4z" fill="#fff"></path><path d="M7 16.5h13m-13 6h14m-14 6h18" stroke="#1060E1" stroke-miterlimit="10"></path><path d="M39 30a14 14 0 1 0 0-28 14 14 0 0 0 0 28z" fill="#FFB935"></path><path d="M50.5 14a13.5 13.5 0 1 1-27 0 13.5 13.5 0 0 1 27 0z" stroke="#F48024" stroke-miterlimit="10"></path><path d="M32.5 21.5v-8h9v8h-9zm2-9.5V9.3A2.5 2.5 0 0 1 37 6.8a2.5 2.5 0 0 1 2.5 2.5V12h-5zm2 3v2m1-2v2" stroke="#fff" stroke-miterlimit="10"></path></svg>
            </div>
        </div>

</div>



        <div id="content" class="snippet-hidden">

            
<div itemprop="mainEntity" itemscope="" itemtype="http://schema.org/Question">
    <link itemprop="image" href="https://cdn.sstatic.net/Sites/stackoverflow/Img/apple-touch-icon.png?v=c78bd457575a">

    <div class="inner-content clearfix">

        

            <div id="question-header" class="grid sm:fd-column">
                        <h1 itemprop="name" class="grid--cell fs-headline1 fl1 ow-break-word mb8"><a href="https://stackoverflow.com/questions/48301186/cropping-concave-polygon-from-image-using-opencv-python" class="question-hyperlink">Cropping Concave polygon from Image using Opencv python</a></h1>

                <div class="ml12 aside-cta grid--cell print:d-none sm:ml0 sm:mb12 sm:order-first sm:as-end">
                    
    <a href="https://stackoverflow.com/questions/ask" class="ws-nowrap s-btn s-btn__primary">
        Ask Question
    </a>

                </div>
            </div>
            <div class="grid fw-wrap pb8 mb16 bb bc-black-2">
                    <div class="grid--cell ws-nowrap mr16 mb8" title="2018-01-17 12:29:10Z">
                        <span class="fc-light mr2">Asked</span>
                        <time itemprop="dateCreated" datetime="2018-01-17T12:29:10">2 years, 7 months ago</time>
                    </div>
                        <div class="grid--cell ws-nowrap mr16 mb8">
                            <span class="fc-light mr2">Active</span>
                            <a href="https://stackoverflow.com/questions/48301186/cropping-concave-polygon-from-image-using-opencv-python?lastactivity" class="s-link s-link__inherit" title="2018-06-01 03:47:04Z">2 years, 3 months ago</a>
                        </div>
                    <div class="grid--cell ws-nowrap mb8" title="Viewed 12,701 times">
                        <span class="fc-light mr2">Viewed</span>
                        13k times
                    </div>
            </div>
            <div id="mainbar" role="main" aria-label="question and answers">

                
<div class="question" data-questionid="48301186" id="question">
    <style>
    </style>
<div class="js-zone-container zone-container-main mb8" style="min-height: auto; height: auto;">
    <div id="dfp-tlb" class="everyonelovesstackoverflow everyoneloves__top-leaderboard everyoneloves__leaderboard" data-dfp-zone="true" data-google-query-id="CJ2u48Kwz-sCFTucSwUd0twMoQ" data-clc-prefilled="true" data-clc-ready="true" style="min-height: auto; height: auto;"><div id="google_ads_iframe_/248424177/stackoverflow.com/lb/question-pages_0__container__" style="border: 0pt none; display: inline-block; width: 728px; height: 90px;"><iframe frameborder="0" src="./none_files/container.html" id="google_ads_iframe_/248424177/stackoverflow.com/lb/question-pages_0" title="3rd party ad content" name="" scrolling="no" marginwidth="0" marginheight="0" width="728" height="90" data-is-safeframe="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-top-navigation-by-user-activation" data-google-container-id="1" style="border: 0px; vertical-align: bottom;" data-load-complete="true"></iframe></div></div>
    <div class="js-report-ad-button-container " style="width: 300px; height: 24px;"><button class="js-report-ad s-btn s-btn__link mt6">Report this ad</button></div>
</div>

    <div class="post-layout">
        <div class="votecell post-layout--left">
            <div class="js-voting-container grid fd-column ai-stretch gs4 fc-black-200" data-post-id="48301186">
        <button class="js-vote-up-btn grid--cell s-btn s-btn__unset c-pointer" data-controller="s-tooltip" data-s-tooltip-placement="right" aria-pressed="false" aria-label="Up vote" data-selected-classes="fc-theme-primary" aria-describedby="--stacks-s-tooltip-a3yai1kz"><svg aria-hidden="true" class="m0 svg-icon iconArrowUpLg" width="36" height="36" viewBox="0 0 36 36"><path d="M2 26h32L18 10 2 26z"></path></svg></button><div id="--stacks-s-tooltip-a3yai1kz" class="s-popover s-popover__tooltip pe-none" aria-hidden="true" role="tooltip">This question shows research effort; it is useful and clear<div class="s-popover--arrow"></div></div>
        <div class="js-vote-count grid--cell fc-black-500 fs-title grid fd-column ai-center" itemprop="upvoteCount" data-value="13">13</div>
        <button class="js-vote-down-btn grid--cell s-btn s-btn__unset c-pointer" data-controller="s-tooltip" data-s-tooltip-placement="right" aria-pressed="false" aria-label="Down vote" data-selected-classes="fc-theme-primary" aria-describedby="--stacks-s-tooltip-kl0laisg"><svg aria-hidden="true" class="m0 svg-icon iconArrowDownLg" width="36" height="36" viewBox="0 0 36 36"><path d="M2 10h32L18 26 2 10z"></path></svg></button><div id="--stacks-s-tooltip-kl0laisg" class="s-popover s-popover__tooltip pe-none" aria-hidden="true" role="tooltip">This question does not show any research effort; it is unclear or not useful<div class="s-popover--arrow"></div></div>

        <button class="js-bookmark-btn s-btn s-btn__unset c-pointer py4 js-gps-track" data-controller="s-tooltip" data-s-tooltip-placement="right" aria-pressed="false" aria-label="Bookmark (12)" data-selected-classes="fc-yellow-600" data-gps-track="post.click({ item: 1, priv: 0, post_type: 1 })" aria-describedby="--stacks-s-tooltip-ih8duvkz">
            <svg aria-hidden="true" class="svg-icon iconBookmark" width="18" height="18" viewBox="0 0 18 18"><path d="M6 1a2 2 0 00-2 2v14l5-4 5 4V3a2 2 0 00-2-2H6zm3.9 3.83h2.9l-2.35 1.7.9 2.77L9 7.59l-2.35 1.7.9-2.76-2.35-1.7h2.9L9 2.06l.9 2.77z"></path></svg>
            <div class="js-bookmark-count mt4" data-value="12">12</div>
        </button><div id="--stacks-s-tooltip-ih8duvkz" class="s-popover s-popover__tooltip pe-none" aria-hidden="true" role="tooltip">Bookmark this question.<div class="s-popover--arrow"></div></div>
    

    
        <a class="js-post-issue grid--cell s-btn s-btn__unset c-pointer py6 mx-auto" href="https://stackoverflow.com/posts/48301186/timeline" data-shortcut="T" data-controller="s-tooltip" data-s-tooltip-placement="right" aria-label="Timeline" aria-describedby="--stacks-s-tooltip-4t0xk1km"><svg aria-hidden="true" class="mln2 mr0 svg-icon iconHistory" width="19" height="18" viewBox="0 0 19 18"><path d="M3 9a8 8 0 113.73 6.77L8.2 14.3A6 6 0 105 9l3.01-.01-4 4-4-4h3L3 9zm7-4h1.01L11 9.36l3.22 2.1-.6.93L10 10V5z"></path></svg></a><div id="--stacks-s-tooltip-4t0xk1km" class="s-popover s-popover__tooltip pe-none" aria-hidden="true" role="tooltip">Show activity on this post.<div class="s-popover--arrow"></div></div>

</div>

        </div>

        

<div class="postcell post-layout--right">
    
    <div class="s-prose js-post-body" itemprop="text">
                    
<p>How can I crop a concave polygon from an image. My Input image look like 
<img src="./none_files/qrJTd.png" alt="this">.</p>

<p>and the coordinates of <strong>closed</strong> polygon are 
[10,150],[150,100],[300,150],[350,100],[310,20],[35,10]. I want region bounded by concave polygon to be cropped using opencv. I searched for other similar questions but I did not able to find correct answer. That's why I am asking it ? Can you help me.</p>

<p>Any help would be highly appreciated.!!!</p>
    </div>

        <div class="post-taglist grid gs4 gsy fd-column">
            <div class="grid ps-relative d-block">
                <a href="https://stackoverflow.com/questions/tagged/python" class="post-tag js-gps-track" title="show questions tagged &#39;python&#39;" rel="tag">python</a> <a href="https://stackoverflow.com/questions/tagged/opencv" class="post-tag js-gps-track" title="show questions tagged &#39;opencv&#39;" rel="tag">opencv</a> <a href="https://stackoverflow.com/questions/tagged/image-processing" class="post-tag js-gps-track" title="show questions tagged &#39;image-processing&#39;" rel="tag">image-processing</a> <a href="https://stackoverflow.com/questions/tagged/crop" class="post-tag js-gps-track" title="show questions tagged &#39;crop&#39;" rel="tag">crop</a> 
            </div>
        </div>

    <div class="mb0 ">
        <div class="mt16 grid gs8 gsy fw-wrap jc-end ai-start pt4">
            <div class="grid--cell mr16" style="flex: 1 1 100px;">
                

<div class="post-menu">
    <a href="https://stackoverflow.com/q/48301186" rel="nofollow" itemprop="url" class="js-share-link js-gps-track" title="short permalink to this question" data-gps-track="post.click({ item: 2, priv: 0, post_type: 1 })" data-controller="se-share-sheet s-popover" data-se-share-sheet-title="Share a link to this question" data-se-share-sheet-subtitle="" data-se-share-sheet-post-type="question" data-se-share-sheet-social="facebook twitter devto" data-se-share-sheet-location="1" data-se-share-sheet-license-url="https%3a%2f%2fcreativecommons.org%2flicenses%2fby-sa%2f3.0%2f" data-se-share-sheet-license-name="CC BY-SA 3.0" data-s-popover-placement="bottom-start" aria-controls="se-share-sheet-0" data-action=" s-popover#toggle se-share-sheet#preventNavigation s-popover:show-&gt;se-share-sheet#willShow s-popover:shown-&gt;se-share-sheet#didShow">share</a><div class="s-popover z-dropdown" style="width: unset; max-width: 28em;" id="se-share-sheet-0"><div class="s-popover--arrow"></div><div><span class="js-title fw-bold">Share a link to this question</span> <span class="js-subtitle"></span></div><div class="my8"><input type="text" class="js-input s-input wmn3 sm:wmn-initial" readonly=""></div><div class="d-flex jc-space-between mbn4"><button class="js-copy-link-btn s-btn s-btn__link">Copy link</button><a href="https://creativecommons.org/licenses/by-sa/3.0/" rel="license" class="s-block-link fc-blue-600 js-license" target="_blank" title="The current license for this post: CC BY-SA 3.0">CC BY-SA 3.0</a><div class="js-social-container"></div></div></div>
        <span class="lsep">|</span>
                <a href="https://stackoverflow.com/posts/48301186/edit" class="suggest-edit-post js-gps-track" data-gps-track="post.click({ item: 6, priv: 0, post_type: 1 })" title="">improve this question</a>
        <span class="lsep">|</span>
    <button id="btnFollowPost-48301186" class="s-btn s-btn__link fc-black-400 h:fc-black-700 pb2 js-follow-post js-follow-question js-gps-track" role="button" data-gps-track="post.click({ item: 14, priv: 0, post_type: 1 })" data-controller="s-tooltip " data-s-tooltip-placement="bottom" data-s-popover-placement="bottom" aria-controls="" aria-describedby="--stacks-s-tooltip-67r8dqou">
        follow
    </button><div id="--stacks-s-tooltip-67r8dqou" class="s-popover s-popover__tooltip pe-none" aria-hidden="true" role="tooltip">Follow this question to receive notifications<div class="s-popover--arrow"></div></div>
        <span class="lsep">|</span>
</div>

            </div>

                <div class="post-signature grid--cell">
<div class="user-info user-hover">
    <div class="user-action-time">
        <a href="https://stackoverflow.com/posts/48301186/revisions" title="show all edits to this post" class="js-gps-track" data-gps-track="post.click({ item: 4, priv: 0, post_type: 1 })">edited <span title="2018-01-17 12:39:00Z" class="relativetime">Jan 17 '18 at 12:39</span></a>
    </div>
    <div class="user-gravatar32">
        <a href="https://stackoverflow.com/users/3547485/kinght-%e9%87%91"><div class="gravatar-wrapper-32"><img src="./none_files/xGJWo.png" alt="" width="32" height="32" class="bar-sm"></div></a>
    </div>
    <div class="user-details">
        <a href="https://stackoverflow.com/users/3547485/kinght-%e9%87%91">Kinght 金</a>
        <div class="-flair">
            <span class="reputation-score" title="reputation score 12,556" dir="ltr">12.6k</span><span title="3 gold badges" aria-hidden="true"><span class="badge1"></span><span class="badgecount">3</span></span><span class="v-visible-sr">3 gold badges</span><span title="39 silver badges" aria-hidden="true"><span class="badge2"></span><span class="badgecount">39</span></span><span class="v-visible-sr">39 silver badges</span><span title="61 bronze badges" aria-hidden="true"><span class="badge3"></span><span class="badgecount">61</span></span><span class="v-visible-sr">61 bronze badges</span>
        </div>
    </div>
</div>                </div>
            <div class="post-signature owner grid--cell">
                <div class="user-info ">
    <div class="user-action-time">
        asked <span title="2018-01-17 12:29:10Z" class="relativetime">Jan 17 '18 at 12:29</span>
    </div>
    <div class="user-gravatar32">
        <a href="https://stackoverflow.com/users/8237470/himanshu-tiwari"><div class="gravatar-wrapper-32"><img src="./none_files/4a402ae2b868537f085d8d4dd8a0c45b" alt="" width="32" height="32" class="bar-sm"></div></a>
    </div>
    <div class="user-details" itemprop="author" itemscope="" itemtype="http://schema.org/Person">
        <a href="https://stackoverflow.com/users/8237470/himanshu-tiwari">Himanshu Tiwari</a><span class="d-none" itemprop="name">Himanshu Tiwari</span>
        <div class="-flair">
            <span class="reputation-score" title="reputation score " dir="ltr">186</span><span title="1 gold badge" aria-hidden="true"><span class="badge1"></span><span class="badgecount">1</span></span><span class="v-visible-sr">1 gold badge</span><span title="1 silver badge" aria-hidden="true"><span class="badge2"></span><span class="badgecount">1</span></span><span class="v-visible-sr">1 silver badge</span><span title="9 bronze badges" aria-hidden="true"><span class="badge3"></span><span class="badgecount">9</span></span><span class="v-visible-sr">9 bronze badges</span>
        </div>
    </div>
</div>

            </div>
        </div>
    </div>
    
</div>




                <div class="post-layout--right">
        <div id="comments-48301186" class="comments js-comments-container bt bc-black-2 mt12 " data-post-id="48301186" data-min-length="15">
            <ul class="comments-list js-comments-list" data-remaining-comments-count="0" data-canpost="false" data-cansee="true" data-comments-unavailable="false" data-addlink-disabled="true">

                        <li id="comment-83586893" class="comment js-comment " data-comment-id="83586893">
        <div class="js-comment-actions comment-actions">
            <div class="comment-score js-comment-edit-hide">
            </div>
        </div>
        <div class="comment-text js-comment-text-and-form">
            <div class="comment-body js-comment-edit-hide">
                
                <span class="comment-copy">can you post the original image?</span>
                
–&nbsp;<a href="https://stackoverflow.com/users/888688/api55" title="9,265 reputation" class="comment-user">api55</a>
                <span class="comment-date" dir="ltr"><a class="comment-link" href="https://stackoverflow.com/questions/48301186/cropping-concave-polygon-from-image-using-opencv-python#comment83586893_48301186"><span title="2018-01-17 12:32:17Z, License: CC BY-SA 3.0" class="relativetime-clean">Jan 17 '18 at 12:32</span></a></span>
            </div>
        </div>
    </li>

            </ul>
	    </div>

        <div id="comments-link-48301186" data-rep="50" data-anon="true">
                    <a class="js-add-link comments-link disabled-link" title="Use comments to ask for more information or suggest improvements. Avoid answering questions in comments." href="https://stackoverflow.com/questions/48301186/cropping-concave-polygon-from-image-using-opencv-python#" role="button">add a comment</a>
                <span class="js-link-separator dno">&nbsp;|&nbsp;</span>
            <a class="js-show-link comments-link dno" title="expand to show all comments on this post" href="https://stackoverflow.com/questions/48301186/cropping-concave-polygon-from-image-using-opencv-python#" onclick="" role="button"></a>
        </div>         
    </div>
    </div>
</div>


<div class="js-zone-container zone-container-responsive">
    <div id="dfp-isb" class="everyonelovesstackoverflow everyoneloves__inline-sidebar mx-auto" style="min-height: auto; height: auto; display: none;"></div>
    <div class="js-report-ad-button-container mx-auto" style="width: 300px"></div>
</div>

                <div id="answers">

                    <a name="tab-top"></a>
                    <div id="answers-header">
                        <div class="answers-subheader grid ai-center mb8">
                            <div class="grid--cell fl1">
                                <h2 class="mb0" data-answercount="2">
                                        2 Answers
                                    <span style="display:none;" itemprop="answerCount">2</span>
                                </h2>
                            </div>
                            <div class="grid--cell">
                                <div class=" grid s-btn-group js-filter-btn">
        <a class="grid--cell s-btn s-btn__muted s-btn__outlined" href="https://stackoverflow.com/questions/48301186/cropping-concave-polygon-from-image-using-opencv-python?answertab=active#tab-top" data-nav-xhref="" title="Answers with the latest activity first" data-value="active" data-shortcut="A">
            Active</a>
        <a class="grid--cell s-btn s-btn__muted s-btn__outlined" href="https://stackoverflow.com/questions/48301186/cropping-concave-polygon-from-image-using-opencv-python?answertab=oldest#tab-top" data-nav-xhref="" title="Answers in the order they were provided" data-value="oldest" data-shortcut="O">
            Oldest</a>
        <a class="youarehere is-selected grid--cell s-btn s-btn__muted s-btn__outlined" href="https://stackoverflow.com/questions/48301186/cropping-concave-polygon-from-image-using-opencv-python?answertab=votes#tab-top" data-nav-xhref="" title="Answers with the highest score first" data-value="votes" data-shortcut="V">
            Votes</a>
</div>

                            </div>
                        </div>
                            
                    </div>


                                          
<a name="48301735"></a>
<div id="answer-48301735" class="answer accepted-answer" data-answerid="48301735" itemprop="acceptedAnswer" itemscope="" itemtype="http://schema.org/Answer">
    <div class="post-layout">
        <div class="votecell post-layout--left">
            <div class="js-voting-container grid fd-column ai-stretch gs4 fc-black-200" data-post-id="48301735">
        <button class="js-vote-up-btn grid--cell s-btn s-btn__unset c-pointer" data-controller="s-tooltip" data-s-tooltip-placement="right" aria-pressed="false" aria-label="Up vote" data-selected-classes="fc-theme-primary" aria-describedby="--stacks-s-tooltip-abhmvflj"><svg aria-hidden="true" class="m0 svg-icon iconArrowUpLg" width="36" height="36" viewBox="0 0 36 36"><path d="M2 26h32L18 10 2 26z"></path></svg></button><div id="--stacks-s-tooltip-abhmvflj" class="s-popover s-popover__tooltip pe-none" aria-hidden="true" role="tooltip">This answer is useful<div class="s-popover--arrow"></div></div>
        <div class="js-vote-count grid--cell fc-black-500 fs-title grid fd-column ai-center" itemprop="upvoteCount" data-value="27">27</div>
        <button class="js-vote-down-btn grid--cell s-btn s-btn__unset c-pointer" data-controller="s-tooltip" data-s-tooltip-placement="right" aria-pressed="false" aria-label="Down vote" data-selected-classes="fc-theme-primary" aria-describedby="--stacks-s-tooltip-oqf7iicd"><svg aria-hidden="true" class="m0 svg-icon iconArrowDownLg" width="36" height="36" viewBox="0 0 36 36"><path d="M2 10h32L18 26 2 10z"></path></svg></button><div id="--stacks-s-tooltip-oqf7iicd" class="s-popover s-popover__tooltip pe-none" aria-hidden="true" role="tooltip">This answer is not useful<div class="s-popover--arrow"></div></div>

    
            <div class="js-accepted-answer-indicator grid--cell fc-green-500 ta-center py4" data-s-tooltip-placement="right" title="Loading when this answer was accepted…" tabindex="0" role="note" aria-label="Accepted">
                <svg aria-hidden="true" class="svg-icon iconCheckmarkLg" width="36" height="36" viewBox="0 0 36 36"><path d="M6 14l8 8L30 6v8L14 30l-8-8v-8z"></path></svg>
            </div>

    
        <a class="js-post-issue grid--cell s-btn s-btn__unset c-pointer py6 mx-auto" href="https://stackoverflow.com/posts/48301735/timeline" data-shortcut="T" data-controller="s-tooltip" data-s-tooltip-placement="right" aria-label="Timeline" aria-describedby="--stacks-s-tooltip-fw5z2i70"><svg aria-hidden="true" class="mln2 mr0 svg-icon iconHistory" width="19" height="18" viewBox="0 0 19 18"><path d="M3 9a8 8 0 113.73 6.77L8.2 14.3A6 6 0 105 9l3.01-.01-4 4-4-4h3L3 9zm7-4h1.01L11 9.36l3.22 2.1-.6.93L10 10V5z"></path></svg></a><div id="--stacks-s-tooltip-fw5z2i70" class="s-popover s-popover__tooltip pe-none" aria-hidden="true" role="tooltip">Show activity on this post.<div class="s-popover--arrow"></div></div>

</div>

        </div>

        

<div class="answercell post-layout--right">
    
    <div class="s-prose js-post-body" itemprop="text">
<blockquote>
<p>Steps</p>
<ol>
<li>find region using the poly points</li>
<li>create mask using the poly points</li>
<li>do mask op to crop</li>
<li>add white bg if needed</li>
</ol>
</blockquote>
<p>The code:</p>
<pre class="lang-py prettyprint prettyprinted" style=""><code><span class="com"># 2018.01.17 20:39:17 CST</span><span class="pln">
</span><span class="com"># 2018.01.17 20:50:35 CST</span><span class="pln">
</span><span class="kwd">import</span><span class="pln"> numpy </span><span class="kwd">as</span><span class="pln"> np
</span><span class="kwd">import</span><span class="pln"> cv2

img </span><span class="pun">=</span><span class="pln"> cv2</span><span class="pun">.</span><span class="pln">imread</span><span class="pun">(</span><span class="str">"test.png"</span><span class="pun">)</span><span class="pln">
pts </span><span class="pun">=</span><span class="pln"> np</span><span class="pun">.</span><span class="pln">array</span><span class="pun">([[</span><span class="lit">10</span><span class="pun">,</span><span class="lit">150</span><span class="pun">],[</span><span class="lit">150</span><span class="pun">,</span><span class="lit">100</span><span class="pun">],[</span><span class="lit">300</span><span class="pun">,</span><span class="lit">150</span><span class="pun">],[</span><span class="lit">350</span><span class="pun">,</span><span class="lit">100</span><span class="pun">],[</span><span class="lit">310</span><span class="pun">,</span><span class="lit">20</span><span class="pun">],[</span><span class="lit">35</span><span class="pun">,</span><span class="lit">10</span><span class="pun">]])</span><span class="pln">

</span><span class="com">## (1) Crop the bounding rect</span><span class="pln">
rect </span><span class="pun">=</span><span class="pln"> cv2</span><span class="pun">.</span><span class="pln">boundingRect</span><span class="pun">(</span><span class="pln">pts</span><span class="pun">)</span><span class="pln">
x</span><span class="pun">,</span><span class="pln">y</span><span class="pun">,</span><span class="pln">w</span><span class="pun">,</span><span class="pln">h </span><span class="pun">=</span><span class="pln"> rect
croped </span><span class="pun">=</span><span class="pln"> img</span><span class="pun">[</span><span class="pln">y</span><span class="pun">:</span><span class="pln">y</span><span class="pun">+</span><span class="pln">h</span><span class="pun">,</span><span class="pln"> x</span><span class="pun">:</span><span class="pln">x</span><span class="pun">+</span><span class="pln">w</span><span class="pun">].</span><span class="pln">copy</span><span class="pun">()</span><span class="pln">

</span><span class="com">## (2) make mask</span><span class="pln">
pts </span><span class="pun">=</span><span class="pln"> pts </span><span class="pun">-</span><span class="pln"> pts</span><span class="pun">.</span><span class="pln">min</span><span class="pun">(</span><span class="pln">axis</span><span class="pun">=</span><span class="lit">0</span><span class="pun">)</span><span class="pln">

mask </span><span class="pun">=</span><span class="pln"> np</span><span class="pun">.</span><span class="pln">zeros</span><span class="pun">(</span><span class="pln">croped</span><span class="pun">.</span><span class="pln">shape</span><span class="pun">[:</span><span class="lit">2</span><span class="pun">],</span><span class="pln"> np</span><span class="pun">.</span><span class="pln">uint8</span><span class="pun">)</span><span class="pln">
cv2</span><span class="pun">.</span><span class="pln">drawContours</span><span class="pun">(</span><span class="pln">mask</span><span class="pun">,</span><span class="pln"> </span><span class="pun">[</span><span class="pln">pts</span><span class="pun">],</span><span class="pln"> </span><span class="pun">-</span><span class="lit">1</span><span class="pun">,</span><span class="pln"> </span><span class="pun">(</span><span class="lit">255</span><span class="pun">,</span><span class="pln"> </span><span class="lit">255</span><span class="pun">,</span><span class="pln"> </span><span class="lit">255</span><span class="pun">),</span><span class="pln"> </span><span class="pun">-</span><span class="lit">1</span><span class="pun">,</span><span class="pln"> cv2</span><span class="pun">.</span><span class="pln">LINE_AA</span><span class="pun">)</span><span class="pln">

</span><span class="com">## (3) do bit-op</span><span class="pln">
dst </span><span class="pun">=</span><span class="pln"> cv2</span><span class="pun">.</span><span class="pln">bitwise_and</span><span class="pun">(</span><span class="pln">croped</span><span class="pun">,</span><span class="pln"> croped</span><span class="pun">,</span><span class="pln"> mask</span><span class="pun">=</span><span class="pln">mask</span><span class="pun">)</span><span class="pln">

</span><span class="com">## (4) add the white background</span><span class="pln">
bg </span><span class="pun">=</span><span class="pln"> np</span><span class="pun">.</span><span class="pln">ones_like</span><span class="pun">(</span><span class="pln">croped</span><span class="pun">,</span><span class="pln"> np</span><span class="pun">.</span><span class="pln">uint8</span><span class="pun">)*</span><span class="lit">255</span><span class="pln">
cv2</span><span class="pun">.</span><span class="pln">bitwise_not</span><span class="pun">(</span><span class="pln">bg</span><span class="pun">,</span><span class="pln">bg</span><span class="pun">,</span><span class="pln"> mask</span><span class="pun">=</span><span class="pln">mask</span><span class="pun">)</span><span class="pln">
dst2 </span><span class="pun">=</span><span class="pln"> bg</span><span class="pun">+</span><span class="pln"> dst


cv2</span><span class="pun">.</span><span class="pln">imwrite</span><span class="pun">(</span><span class="str">"croped.png"</span><span class="pun">,</span><span class="pln"> croped</span><span class="pun">)</span><span class="pln">
cv2</span><span class="pun">.</span><span class="pln">imwrite</span><span class="pun">(</span><span class="str">"mask.png"</span><span class="pun">,</span><span class="pln"> mask</span><span class="pun">)</span><span class="pln">
cv2</span><span class="pun">.</span><span class="pln">imwrite</span><span class="pun">(</span><span class="str">"dst.png"</span><span class="pun">,</span><span class="pln"> dst</span><span class="pun">)</span><span class="pln">
cv2</span><span class="pun">.</span><span class="pln">imwrite</span><span class="pun">(</span><span class="str">"dst2.png"</span><span class="pun">,</span><span class="pln"> dst2</span><span class="pun">)</span></code></pre>
<hr>
<p>Source image:</p>
<p><a href="./none_files/kyBXv.png" rel="noreferrer"><img src="./none_files/kyBXv.png" alt="enter image description here"></a></p>
<p>Result:</p>
<p><a href="./none_files/Mg78c.png" rel="noreferrer"><img src="./none_files/Mg78c.png" alt="enter image description here"></a></p>
    </div>
    <div class="grid mb0 fw-wrap ai-start jc-end gs8 gsy">
        <time itemprop="dateCreated" datetime="2018-01-17T12:56:15"></time>
        <div class="grid--cell mr16" style="flex: 1 1 100px;">
            

<div class="post-menu">
    <a href="https://stackoverflow.com/a/48301735" rel="nofollow" itemprop="url" class="js-share-link js-gps-track" title="short permalink to this answer" data-gps-track="post.click({ item: 2, priv: 0, post_type: 2 })" data-controller="se-share-sheet s-popover" data-se-share-sheet-title="Share a link to this answer" data-se-share-sheet-subtitle="" data-se-share-sheet-post-type="answer" data-se-share-sheet-social="facebook twitter devto" data-se-share-sheet-location="2" data-se-share-sheet-license-url="https%3a%2f%2fcreativecommons.org%2flicenses%2fby-sa%2f3.0%2f" data-se-share-sheet-license-name="CC BY-SA 3.0" data-s-popover-placement="bottom-start" aria-controls="se-share-sheet-1" data-action=" s-popover#toggle se-share-sheet#preventNavigation s-popover:show-&gt;se-share-sheet#willShow s-popover:shown-&gt;se-share-sheet#didShow">share</a><div class="s-popover z-dropdown" style="width: unset; max-width: 28em;" id="se-share-sheet-1"><div class="s-popover--arrow"></div><div><span class="js-title fw-bold">Share a link to this answer</span> <span class="js-subtitle"></span></div><div class="my8"><input type="text" class="js-input s-input wmn3 sm:wmn-initial" readonly=""></div><div class="d-flex jc-space-between mbn4"><button class="js-copy-link-btn s-btn s-btn__link">Copy link</button><a href="https://creativecommons.org/licenses/by-sa/3.0/" rel="license" class="s-block-link fc-blue-600 js-license" target="_blank" title="The current license for this post: CC BY-SA 3.0">CC BY-SA 3.0</a><div class="js-social-container"></div></div></div>
        <span class="lsep">|</span>
                <a href="https://stackoverflow.com/posts/48301735/edit" class="suggest-edit-post js-gps-track" data-gps-track="post.click({ item: 6, priv: 0, post_type: 2 })" title="">improve this answer</a>
        <span class="lsep">|</span>
    <button id="btnFollowPost-48301735" class="s-btn s-btn__link fc-black-400 h:fc-black-700 pb2 js-follow-post js-follow-answer js-gps-track" role="button" data-gps-track="post.click({ item: 14, priv: 0, post_type: 2 })" data-controller="s-tooltip " data-s-tooltip-placement="bottom" data-s-popover-placement="bottom" aria-controls="" aria-describedby="--stacks-s-tooltip-s8yrjm49">
        follow
    </button><div id="--stacks-s-tooltip-s8yrjm49" class="s-popover s-popover__tooltip pe-none" aria-hidden="true" role="tooltip">Follow this answer to receive notifications<div class="s-popover--arrow"></div></div>
        <span class="lsep">|</span>
</div>

        </div>
    <div class="post-signature grid--cell fl0">
<div class="user-info user-hover">
    <div class="user-action-time">
        <a href="https://stackoverflow.com/posts/48301735/revisions" title="show all edits to this post" class="js-gps-track" data-gps-track="post.click({ item: 4, priv: 0, post_type: 2 })">edited <span title="2020-06-20 09:12:55Z" class="relativetime">Jun 20 at 9:12</span></a>
    </div>
    <div class="user-gravatar32">
        <a href="https://stackoverflow.com/users/-1/community"><div class="gravatar-wrapper-32"><img src="./none_files/a007be5a61f6aa8f3e85ae2fc18dd66e.png" alt="" width="32" height="32" class="bar-sm"></div></a>
    </div>
    <div class="user-details">
        <a href="https://stackoverflow.com/users/-1/community">Community</a><span class="mod-flair " title="moderator">♦</span>
        <div class="-flair">
            <span class="reputation-score" title="reputation score " dir="ltr">1</span><span title="1 silver badge" aria-hidden="true"><span class="badge2"></span><span class="badgecount">1</span></span><span class="v-visible-sr">1 silver badge</span>
        </div>
    </div>
</div>    </div>


    <div class="post-signature grid--cell fl0">
        <div class="user-info user-hover">
    <div class="user-action-time">
        answered <span title="2018-01-17 12:56:15Z" class="relativetime">Jan 17 '18 at 12:56</span>
    </div>
    <div class="user-gravatar32">
        <a href="https://stackoverflow.com/users/3547485/kinght-%e9%87%91"><div class="gravatar-wrapper-32"><img src="./none_files/xGJWo.png" alt="" width="32" height="32" class="bar-sm"></div></a>
    </div>
    <div class="user-details" itemprop="author" itemscope="" itemtype="http://schema.org/Person">
        <a href="https://stackoverflow.com/users/3547485/kinght-%e9%87%91">Kinght 金</a><span class="d-none" itemprop="name">Kinght 金</span>
        <div class="-flair">
            <span class="reputation-score" title="reputation score 12,556" dir="ltr">12.6k</span><span title="3 gold badges" aria-hidden="true"><span class="badge1"></span><span class="badgecount">3</span></span><span class="v-visible-sr">3 gold badges</span><span title="39 silver badges" aria-hidden="true"><span class="badge2"></span><span class="badgecount">39</span></span><span class="v-visible-sr">39 silver badges</span><span title="61 bronze badges" aria-hidden="true"><span class="badge3"></span><span class="badgecount">61</span></span><span class="v-visible-sr">61 bronze badges</span>
        </div>
    </div>
</div>

    </div>
    </div>
    
</div>




                <div class="post-layout--right">
        <div id="comments-48301735" class="comments js-comments-container bt bc-black-2 mt12 " data-post-id="48301735" data-min-length="15">
            <ul class="comments-list js-comments-list" data-remaining-comments-count="0" data-canpost="false" data-cansee="true" data-comments-unavailable="false" data-addlink-disabled="true">

                        <li id="comment-84863663" class="comment js-comment " data-comment-id="84863663">
        <div class="js-comment-actions comment-actions">
            <div class="comment-score js-comment-edit-hide">
            </div>
        </div>
        <div class="comment-text js-comment-text-and-form">
            <div class="comment-body js-comment-edit-hide">
                
                <span class="comment-copy">How to change the black region in background to "white region" after cropping?</span>
                
–&nbsp;<a href="https://stackoverflow.com/users/8237470/himanshu-tiwari" title="186 reputation" class="comment-user owner">Himanshu Tiwari</a>
                <span class="comment-date" dir="ltr"><a class="comment-link" href="https://stackoverflow.com/questions/48301186/cropping-concave-polygon-from-image-using-opencv-python#comment84863663_48301735"><span title="2018-02-22 13:31:09Z, License: CC BY-SA 3.0" class="relativetime-clean">Feb 22 '18 at 13:31</span></a></span>
            </div>
        </div>
    </li>
    <li id="comment-111175222" class="comment js-comment " data-comment-id="111175222">
        <div class="js-comment-actions comment-actions">
            <div class="comment-score js-comment-edit-hide">
            </div>
        </div>
        <div class="comment-text js-comment-text-and-form">
            <div class="comment-body js-comment-edit-hide">
                
                <span class="comment-copy">is it possible to save the image without background? I mean just save that cropped region only .. ?</span>
                
–&nbsp;<a href="https://stackoverflow.com/users/12193985/abuomair" title="131 reputation" class="comment-user">AbuOmair</a>
                <span class="comment-date" dir="ltr"><a class="comment-link" href="https://stackoverflow.com/questions/48301186/cropping-concave-polygon-from-image-using-opencv-python#comment111175222_48301735"><span title="2020-07-13 03:41:15Z, License: CC BY-SA 4.0" class="relativetime-clean">Jul 13 at 3:41</span></a></span>
            </div>
        </div>
    </li>

            </ul>
	    </div>

        <div id="comments-link-48301735" data-rep="50" data-anon="true">
                    <a class="js-add-link comments-link disabled-link" title="Use comments to ask for more information or suggest improvements. Avoid comments like “+1” or “thanks”." href="https://stackoverflow.com/questions/48301186/cropping-concave-polygon-from-image-using-opencv-python#" role="button">add a comment</a>
                <span class="js-link-separator dno">&nbsp;|&nbsp;</span>
            <a class="js-show-link comments-link dno" title="expand to show all comments on this post" href="https://stackoverflow.com/questions/48301186/cropping-concave-polygon-from-image-using-opencv-python#" onclick="" role="button"></a>
        </div>         
    </div>
    </div>
</div>

<div class="js-zone-container zone-container-main">
    <div id="dfp-mlb" class="everyonelovesstackoverflow everyoneloves__mid-leaderboard everyoneloves__leaderboard" data-clc-prefilled="true" data-google-query-id="COC45MKwz-sCFaeeSwUdsnkE8g" data-clc-ready="true" style="min-height: auto; height: auto; display: none;"><div id="google_ads_iframe_/248424177/stackoverflow.com/mlb/question-pages_0__container__" style="border: 0pt none; width: 728px; height: auto; min-height: auto; display: none;"></div></div>
    <div class="js-report-ad-button-container " style="width: 300px"></div>
</div>
                                          
<a name="48301637"></a>
<div id="answer-48301637" class="answer" data-answerid="48301637" itemprop="suggestedAnswer" itemscope="" itemtype="http://schema.org/Answer">
    <div class="post-layout">
        <div class="votecell post-layout--left">
            <div class="js-voting-container grid fd-column ai-stretch gs4 fc-black-200" data-post-id="48301637">
        <button class="js-vote-up-btn grid--cell s-btn s-btn__unset c-pointer" data-controller="s-tooltip" data-s-tooltip-placement="right" aria-pressed="false" aria-label="Up vote" data-selected-classes="fc-theme-primary" aria-describedby="--stacks-s-tooltip-9r35zqix"><svg aria-hidden="true" class="m0 svg-icon iconArrowUpLg" width="36" height="36" viewBox="0 0 36 36"><path d="M2 26h32L18 10 2 26z"></path></svg></button><div id="--stacks-s-tooltip-9r35zqix" class="s-popover s-popover__tooltip pe-none" aria-hidden="true" role="tooltip">This answer is useful<div class="s-popover--arrow"></div></div>
        <div class="js-vote-count grid--cell fc-black-500 fs-title grid fd-column ai-center" itemprop="upvoteCount" data-value="9">9</div>
        <button class="js-vote-down-btn grid--cell s-btn s-btn__unset c-pointer" data-controller="s-tooltip" data-s-tooltip-placement="right" aria-pressed="false" aria-label="Down vote" data-selected-classes="fc-theme-primary" aria-describedby="--stacks-s-tooltip-mcbwq7vg"><svg aria-hidden="true" class="m0 svg-icon iconArrowDownLg" width="36" height="36" viewBox="0 0 36 36"><path d="M2 10h32L18 26 2 10z"></path></svg></button><div id="--stacks-s-tooltip-mcbwq7vg" class="s-popover s-popover__tooltip pe-none" aria-hidden="true" role="tooltip">This answer is not useful<div class="s-popover--arrow"></div></div>

    
            <div class="js-accepted-answer-indicator grid--cell fc-green-500 ta-center py4 d-none" data-s-tooltip-placement="right" title="Loading when this answer was accepted…" tabindex="0" role="note" aria-label="Accepted">
                <svg aria-hidden="true" class="svg-icon iconCheckmarkLg" width="36" height="36" viewBox="0 0 36 36"><path d="M6 14l8 8L30 6v8L14 30l-8-8v-8z"></path></svg>
            </div>

    
        <a class="js-post-issue grid--cell s-btn s-btn__unset c-pointer py6 mx-auto" href="https://stackoverflow.com/posts/48301637/timeline" data-shortcut="T" data-controller="s-tooltip" data-s-tooltip-placement="right" aria-label="Timeline" aria-describedby="--stacks-s-tooltip-wmu1buif"><svg aria-hidden="true" class="mln2 mr0 svg-icon iconHistory" width="19" height="18" viewBox="0 0 19 18"><path d="M3 9a8 8 0 113.73 6.77L8.2 14.3A6 6 0 105 9l3.01-.01-4 4-4-4h3L3 9zm7-4h1.01L11 9.36l3.22 2.1-.6.93L10 10V5z"></path></svg></a><div id="--stacks-s-tooltip-wmu1buif" class="s-popover s-popover__tooltip pe-none" aria-hidden="true" role="tooltip">Show activity on this post.<div class="s-popover--arrow"></div></div>

</div>

        </div>

        

<div class="answercell post-layout--right">
    
    <div class="s-prose js-post-body" itemprop="text">
<p>You can do it in 3 steps:</p>

<p>1) Create a mask out of the image</p>

<pre class="lang-py prettyprint prettyprinted" style=""><code><span class="pln">mask </span><span class="pun">=</span><span class="pln"> np</span><span class="pun">.</span><span class="pln">zeros</span><span class="pun">((</span><span class="pln">height</span><span class="pun">,</span><span class="pln"> width</span><span class="pun">))</span><span class="pln">
points </span><span class="pun">=</span><span class="pln"> np</span><span class="pun">.</span><span class="pln">array</span><span class="pun">([[[</span><span class="lit">10</span><span class="pun">,</span><span class="lit">150</span><span class="pun">],[</span><span class="lit">150</span><span class="pun">,</span><span class="lit">100</span><span class="pun">],[</span><span class="lit">300</span><span class="pun">,</span><span class="lit">150</span><span class="pun">],[</span><span class="lit">350</span><span class="pun">,</span><span class="lit">100</span><span class="pun">],[</span><span class="lit">310</span><span class="pun">,</span><span class="lit">20</span><span class="pun">],[</span><span class="lit">35</span><span class="pun">,</span><span class="lit">10</span><span class="pun">]]])</span><span class="pln">
cv2</span><span class="pun">.</span><span class="pln">fillPoly</span><span class="pun">(</span><span class="pln">mask</span><span class="pun">,</span><span class="pln"> points</span><span class="pun">,</span><span class="pln"> </span><span class="pun">(</span><span class="lit">255</span><span class="pun">))</span></code></pre>

<p>2) Apply mask to original image</p>

<pre class="lang-py prettyprint prettyprinted" style=""><code><span class="pln">res </span><span class="pun">=</span><span class="pln"> cv2</span><span class="pun">.</span><span class="pln">bitwise_and</span><span class="pun">(</span><span class="pln">img</span><span class="pun">,</span><span class="pln">img</span><span class="pun">,</span><span class="pln">mask </span><span class="pun">=</span><span class="pln"> mask</span><span class="pun">)</span></code></pre>

<p>3) Optionally you can remove the crop the image to have a smaller one</p>

<pre class="lang-py prettyprint prettyprinted" style=""><code><span class="pln">rect </span><span class="pun">=</span><span class="pln"> cv2</span><span class="pun">.</span><span class="pln">boundingRect</span><span class="pun">(</span><span class="pln">points</span><span class="pun">)</span><span class="pln"> </span><span class="com"># returns (x,y,w,h) of the rect</span><span class="pln">
cropped </span><span class="pun">=</span><span class="pln"> res</span><span class="pun">[</span><span class="pln">rect</span><span class="pun">[</span><span class="lit">1</span><span class="pun">]:</span><span class="pln"> rect</span><span class="pun">[</span><span class="lit">1</span><span class="pun">]</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> rect</span><span class="pun">[</span><span class="lit">3</span><span class="pun">],</span><span class="pln"> rect</span><span class="pun">[</span><span class="lit">0</span><span class="pun">]:</span><span class="pln"> rect</span><span class="pun">[</span><span class="lit">0</span><span class="pun">]</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> rect</span><span class="pun">[</span><span class="lit">2</span><span class="pun">]]</span></code></pre>

<p>With this you should have at the end the image cropped</p>

<h1>UPDATE</h1>

<p>For the sake of completeness here is the complete code:</p>

<pre class="lang-py prettyprint prettyprinted" style=""><code><span class="kwd">import</span><span class="pln"> numpy </span><span class="kwd">as</span><span class="pln"> np
</span><span class="kwd">import</span><span class="pln"> cv2

img </span><span class="pun">=</span><span class="pln"> cv2</span><span class="pun">.</span><span class="pln">imread</span><span class="pun">(</span><span class="str">"test.png"</span><span class="pun">)</span><span class="pln">
height </span><span class="pun">=</span><span class="pln"> img</span><span class="pun">.</span><span class="pln">shape</span><span class="pun">[</span><span class="lit">0</span><span class="pun">]</span><span class="pln">
width </span><span class="pun">=</span><span class="pln"> img</span><span class="pun">.</span><span class="pln">shape</span><span class="pun">[</span><span class="lit">1</span><span class="pun">]</span><span class="pln">

mask </span><span class="pun">=</span><span class="pln"> np</span><span class="pun">.</span><span class="pln">zeros</span><span class="pun">((</span><span class="pln">height</span><span class="pun">,</span><span class="pln"> width</span><span class="pun">),</span><span class="pln"> dtype</span><span class="pun">=</span><span class="pln">np</span><span class="pun">.</span><span class="pln">uint8</span><span class="pun">)</span><span class="pln">
points </span><span class="pun">=</span><span class="pln"> np</span><span class="pun">.</span><span class="pln">array</span><span class="pun">([[[</span><span class="lit">10</span><span class="pun">,</span><span class="lit">150</span><span class="pun">],[</span><span class="lit">150</span><span class="pun">,</span><span class="lit">100</span><span class="pun">],[</span><span class="lit">300</span><span class="pun">,</span><span class="lit">150</span><span class="pun">],[</span><span class="lit">350</span><span class="pun">,</span><span class="lit">100</span><span class="pun">],[</span><span class="lit">310</span><span class="pun">,</span><span class="lit">20</span><span class="pun">],[</span><span class="lit">35</span><span class="pun">,</span><span class="lit">10</span><span class="pun">]]])</span><span class="pln">
cv2</span><span class="pun">.</span><span class="pln">fillPoly</span><span class="pun">(</span><span class="pln">mask</span><span class="pun">,</span><span class="pln"> points</span><span class="pun">,</span><span class="pln"> </span><span class="pun">(</span><span class="lit">255</span><span class="pun">))</span><span class="pln">

res </span><span class="pun">=</span><span class="pln"> cv2</span><span class="pun">.</span><span class="pln">bitwise_and</span><span class="pun">(</span><span class="pln">img</span><span class="pun">,</span><span class="pln">img</span><span class="pun">,</span><span class="pln">mask </span><span class="pun">=</span><span class="pln"> mask</span><span class="pun">)</span><span class="pln">

rect </span><span class="pun">=</span><span class="pln"> cv2</span><span class="pun">.</span><span class="pln">boundingRect</span><span class="pun">(</span><span class="pln">points</span><span class="pun">)</span><span class="pln"> </span><span class="com"># returns (x,y,w,h) of the rect</span><span class="pln">
cropped </span><span class="pun">=</span><span class="pln"> res</span><span class="pun">[</span><span class="pln">rect</span><span class="pun">[</span><span class="lit">1</span><span class="pun">]:</span><span class="pln"> rect</span><span class="pun">[</span><span class="lit">1</span><span class="pun">]</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> rect</span><span class="pun">[</span><span class="lit">3</span><span class="pun">],</span><span class="pln"> rect</span><span class="pun">[</span><span class="lit">0</span><span class="pun">]:</span><span class="pln"> rect</span><span class="pun">[</span><span class="lit">0</span><span class="pun">]</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> rect</span><span class="pun">[</span><span class="lit">2</span><span class="pun">]]</span><span class="pln">

cv2</span><span class="pun">.</span><span class="pln">imshow</span><span class="pun">(</span><span class="str">"cropped"</span><span class="pln"> </span><span class="pun">,</span><span class="pln"> cropped </span><span class="pun">)</span><span class="pln">
cv2</span><span class="pun">.</span><span class="pln">imshow</span><span class="pun">(</span><span class="str">"same size"</span><span class="pln"> </span><span class="pun">,</span><span class="pln"> res</span><span class="pun">)</span><span class="pln">
cv2</span><span class="pun">.</span><span class="pln">waitKey</span><span class="pun">(</span><span class="lit">0</span><span class="pun">)</span></code></pre>
    </div>
    <div class="grid mb0 fw-wrap ai-start jc-end gs8 gsy">
        <time itemprop="dateCreated" datetime="2018-01-17T12:51:56"></time>
        <div class="grid--cell mr16" style="flex: 1 1 100px;">
            

<div class="post-menu">
    <a href="https://stackoverflow.com/a/48301637" rel="nofollow" itemprop="url" class="js-share-link js-gps-track" title="short permalink to this answer" data-gps-track="post.click({ item: 2, priv: 0, post_type: 2 })" data-controller="se-share-sheet s-popover" data-se-share-sheet-title="Share a link to this answer" data-se-share-sheet-subtitle="" data-se-share-sheet-post-type="answer" data-se-share-sheet-social="facebook twitter devto" data-se-share-sheet-location="2" data-se-share-sheet-license-url="https%3a%2f%2fcreativecommons.org%2flicenses%2fby-sa%2f3.0%2f" data-se-share-sheet-license-name="CC BY-SA 3.0" data-s-popover-placement="bottom-start" aria-controls="se-share-sheet-2" data-action=" s-popover#toggle se-share-sheet#preventNavigation s-popover:show-&gt;se-share-sheet#willShow s-popover:shown-&gt;se-share-sheet#didShow">share</a><div class="s-popover z-dropdown" style="width: unset; max-width: 28em;" id="se-share-sheet-2"><div class="s-popover--arrow"></div><div><span class="js-title fw-bold">Share a link to this answer</span> <span class="js-subtitle"></span></div><div class="my8"><input type="text" class="js-input s-input wmn3 sm:wmn-initial" readonly=""></div><div class="d-flex jc-space-between mbn4"><button class="js-copy-link-btn s-btn s-btn__link">Copy link</button><a href="https://creativecommons.org/licenses/by-sa/3.0/" rel="license" class="s-block-link fc-blue-600 js-license" target="_blank" title="The current license for this post: CC BY-SA 3.0">CC BY-SA 3.0</a><div class="js-social-container"></div></div></div>
        <span class="lsep">|</span>
                <a href="https://stackoverflow.com/posts/48301637/edit" class="suggest-edit-post js-gps-track" data-gps-track="post.click({ item: 6, priv: 0, post_type: 2 })" title="">improve this answer</a>
        <span class="lsep">|</span>
    <button id="btnFollowPost-48301637" class="s-btn s-btn__link fc-black-400 h:fc-black-700 pb2 js-follow-post js-follow-answer js-gps-track" role="button" data-gps-track="post.click({ item: 14, priv: 0, post_type: 2 })" data-controller="s-tooltip " data-s-tooltip-placement="bottom" data-s-popover-placement="bottom" aria-controls="" aria-describedby="--stacks-s-tooltip-o2s4ddym">
        follow
    </button><div id="--stacks-s-tooltip-o2s4ddym" class="s-popover s-popover__tooltip pe-none" aria-hidden="true" role="tooltip">Follow this answer to receive notifications<div class="s-popover--arrow"></div></div>
        <span class="lsep">|</span>
</div>

        </div>
    <div class="post-signature grid--cell fl0">
<div class="user-info ">
    <div class="user-action-time">
        <a href="https://stackoverflow.com/posts/48301637/revisions" title="show all edits to this post" class="js-gps-track" data-gps-track="post.click({ item: 4, priv: 0, post_type: 2 })">edited <span title="2018-01-17 13:54:10Z" class="relativetime">Jan 17 '18 at 13:54</span></a>
    </div>
    <div class="user-gravatar32">
        
    </div>
    <div class="user-details">
        
        <div class="-flair">
            
        </div>
    </div>
</div>    </div>


    <div class="post-signature grid--cell fl0">
        <div class="user-info user-hover">
    <div class="user-action-time">
        answered <span title="2018-01-17 12:51:56Z" class="relativetime">Jan 17 '18 at 12:51</span>
    </div>
    <div class="user-gravatar32">
        <a href="https://stackoverflow.com/users/888688/api55"><div class="gravatar-wrapper-32"><img src="./none_files/4e1a439c266dcf5015373dbeae410ff5.jpeg" alt="" width="32" height="32" class="bar-sm"></div></a>
    </div>
    <div class="user-details" itemprop="author" itemscope="" itemtype="http://schema.org/Person">
        <a href="https://stackoverflow.com/users/888688/api55">api55</a><span class="d-none" itemprop="name">api55</span>
        <div class="-flair">
            <span class="reputation-score" title="reputation score " dir="ltr">9,265</span><span title="4 gold badges" aria-hidden="true"><span class="badge1"></span><span class="badgecount">4</span></span><span class="v-visible-sr">4 gold badges</span><span title="34 silver badges" aria-hidden="true"><span class="badge2"></span><span class="badgecount">34</span></span><span class="v-visible-sr">34 silver badges</span><span title="50 bronze badges" aria-hidden="true"><span class="badge3"></span><span class="badgecount">50</span></span><span class="v-visible-sr">50 bronze badges</span>
        </div>
    </div>
</div>

    </div>
    </div>
    
</div>




                <div class="post-layout--right">
        <div id="comments-48301637" class="comments js-comments-container bt bc-black-2 mt12 " data-post-id="48301637" data-min-length="15">
            <ul class="comments-list js-comments-list" data-remaining-comments-count="0" data-canpost="false" data-cansee="true" data-comments-unavailable="false" data-addlink-disabled="true">

                        <li id="comment-83588856" class="comment js-comment " data-comment-id="83588856">
        <div class="js-comment-actions comment-actions">
            <div class="comment-score js-comment-edit-hide">
            </div>
        </div>
        <div class="comment-text js-comment-text-and-form">
            <div class="comment-body js-comment-edit-hide">
                
                <span class="comment-copy">I tried with your code but the output that I am getting is the cropped convex shape not concave shape. My problem has been resolved with @Silencer answer. Thanks for your answer too.                                                     P.S. - Can't insert image in comment!!</span>
                
–&nbsp;<a href="https://stackoverflow.com/users/8237470/himanshu-tiwari" title="186 reputation" class="comment-user owner">Himanshu Tiwari</a>
                <span class="comment-date" dir="ltr"><a class="comment-link" href="https://stackoverflow.com/questions/48301186/cropping-concave-polygon-from-image-using-opencv-python#comment83588856_48301637"><span title="2018-01-17 13:22:35Z, License: CC BY-SA 3.0" class="relativetime-clean">Jan 17 '18 at 13:22</span></a></span>
                        <span title="this comment was edited 2 times">
                            <svg aria-hidden="true" class="va-text-bottom o50 svg-icon iconPencilSm" width="14" height="14" viewBox="0 0 14 14"><path d="M11.1 1.71l1.13 1.12c.2.2.2.51 0 .71L11.1 4.7 9.21 2.86l1.17-1.15c.2-.2.51-.2.71 0zM2 10.12l6.37-6.43 1.88 1.88L3.88 12H2v-1.88z"></path></svg>
                        </span>
            </div>
        </div>
    </li>
    <li id="comment-83589741" class="comment js-comment " data-comment-id="83589741">
        <div class="js-comment-actions comment-actions">
            <div class="comment-score js-comment-edit-hide">
            </div>
        </div>
        <div class="comment-text js-comment-text-and-form">
            <div class="comment-body js-comment-edit-hide">
                
                <span class="comment-copy">@HimanshuTiwari I do not understand... this should work for any polygon convex or concave... and basically both answer do almost the same, I tested my code with a random image and I got the same result as Silencer... oh well, if you manage to solve it, then everything is good</span>
                
–&nbsp;<a href="https://stackoverflow.com/users/888688/api55" title="9,265 reputation" class="comment-user">api55</a>
                <span class="comment-date" dir="ltr"><a class="comment-link" href="https://stackoverflow.com/questions/48301186/cropping-concave-polygon-from-image-using-opencv-python#comment83589741_48301637"><span title="2018-01-17 13:43:24Z, License: CC BY-SA 3.0" class="relativetime-clean">Jan 17 '18 at 13:43</span></a></span>
            </div>
        </div>
    </li>
    <li id="comment-83595343" class="comment js-comment " data-comment-id="83595343">
        <div class="js-comment-actions comment-actions">
            <div class="comment-score js-comment-edit-hide">
            </div>
        </div>
        <div class="comment-text js-comment-text-and-form">
            <div class="comment-body js-comment-edit-hide">
                
                <span class="comment-copy">Sorry I did mistake. But now I got the correct output.</span>
                
–&nbsp;<a href="https://stackoverflow.com/users/8237470/himanshu-tiwari" title="186 reputation" class="comment-user owner">Himanshu Tiwari</a>
                <span class="comment-date" dir="ltr"><a class="comment-link" href="https://stackoverflow.com/questions/48301186/cropping-concave-polygon-from-image-using-opencv-python#comment83595343_48301637"><span title="2018-01-17 15:59:07Z, License: CC BY-SA 3.0" class="relativetime-clean">Jan 17 '18 at 15:59</span></a></span>
            </div>
        </div>
    </li>
    <li id="comment-83598394" class="comment js-comment " data-comment-id="83598394">
        <div class="js-comment-actions comment-actions">
            <div class="comment-score js-comment-edit-hide">
            </div>
        </div>
        <div class="comment-text js-comment-text-and-form">
            <div class="comment-body js-comment-edit-hide">
                
                <span class="comment-copy">@HimanshuTiwari It is ok :) it is always good to have 2 possible result to choose from :)</span>
                
–&nbsp;<a href="https://stackoverflow.com/users/888688/api55" title="9,265 reputation" class="comment-user">api55</a>
                <span class="comment-date" dir="ltr"><a class="comment-link" href="https://stackoverflow.com/questions/48301186/cropping-concave-polygon-from-image-using-opencv-python#comment83598394_48301637"><span title="2018-01-17 17:18:27Z, License: CC BY-SA 3.0" class="relativetime-clean">Jan 17 '18 at 17:18</span></a></span>
            </div>
        </div>
    </li>
    <li id="comment-92125476" class="comment js-comment " data-comment-id="92125476">
        <div class="js-comment-actions comment-actions">
            <div class="comment-score js-comment-edit-hide">
                    <span title="number of &#39;useful comment&#39; votes received" class="cool">2</span>
            </div>
        </div>
        <div class="comment-text js-comment-text-and-form">
            <div class="comment-body js-comment-edit-hide">
                
                <span class="comment-copy">@HimanshuTiwari Even if there are two answers to choose from both deserve the merit of acceptance as well as thumbs UP. I found both useful and well readable so +1 for both of them.</span>
                
–&nbsp;<a href="https://stackoverflow.com/users/5396082/skr" title="151 reputation" class="comment-user">SKR</a>
                <span class="comment-date" dir="ltr"><a class="comment-link" href="https://stackoverflow.com/questions/48301186/cropping-concave-polygon-from-image-using-opencv-python#comment92125476_48301637"><span title="2018-10-01 16:40:01Z, License: CC BY-SA 4.0" class="relativetime-clean">Oct 1 '18 at 16:40</span></a></span>
            </div>
        </div>
    </li>

            </ul>
	    </div>

        <div id="comments-link-48301637" data-rep="50" data-anon="true">
                    <a class="js-add-link comments-link disabled-link" title="Use comments to ask for more information or suggest improvements. Avoid comments like “+1” or “thanks”." href="https://stackoverflow.com/questions/48301186/cropping-concave-polygon-from-image-using-opencv-python#" role="button">add a comment</a>
                <span class="js-link-separator dno">&nbsp;|&nbsp;</span>
            <a class="js-show-link comments-link dno" title="expand to show all comments on this post" href="https://stackoverflow.com/questions/48301186/cropping-concave-polygon-from-image-using-opencv-python#" onclick="" role="button"></a>
        </div>         
    </div>
    </div>
</div>


                        <a name="new-answer"></a>
                            <form id="post-form" action="https://stackoverflow.com/questions/48301186/answer/submit" method="post" class="js-add-answer-component post-form">
                                <input type="hidden" id="post-id" value="48301186">
                                <input type="hidden" id="qualityBanWarningShown" name="qualityBanWarningShown" value="false">
                                <input type="hidden" name="referrer" value="https://www.google.com/">
                                <h2 class="space">
                                    Your Answer
                                </h2>
                                    

    <script>
        StackExchange.ifUsing("editor", function () {
            StackExchange.using("externalEditor", function () {
                StackExchange.using("snippets", function () {
                    StackExchange.snippets.init();
                });
            });
        }, "code-snippets");
    </script>


<script>
    StackExchange.ready(function() {
        var channelOptions = {
            tags: "".split(" "),
            id: "1"
        };
        initTagRenderer("".split(" "), "".split(" "), channelOptions);

        StackExchange.using("externalEditor", function() {
            // Have to fire editor after snippets, if snippets enabled
            if (StackExchange.settings.snippets.snippetsEnabled) {
                StackExchange.using("snippets", function() {
                    createEditor();
                });
            }
            else {
                createEditor();
            }
        });

        function createEditor() {
            StackExchange.prepareEditor({
                heartbeatType: 'answer',
                autoActivateHeartbeat: false,
                convertImagesToLinks: true,
                noModals: true,
                showLowRepImageUploadWarning: true,
                reputationToPostImages: 10,
                bindNavPrevention: true,
                postfix: "",
                imageUploader: {
                brandingHtml: "Powered by \u003ca href=\"https://imgur.com/\"\u003e\u003csvg class=\"svg-icon\" width=\"50\" height=\"18\" viewBox=\"0 0 50 18\" fill=\"none\" xmlns=\"http://www.w3.org/2000/svg\"\u003e\u003cpath d=\"M46.1709 9.17788C46.1709 8.26454 46.2665 7.94324 47.1084 7.58816C47.4091 7.46349 47.7169 7.36433 48.0099 7.26993C48.9099 6.97997 49.672 6.73443 49.672 5.93063C49.672 5.22043 48.9832 4.61182 48.1414 4.61182C47.4335 4.61182 46.7256 4.91628 46.0943 5.50789C45.7307 4.9328 45.2525 4.66231 44.6595 4.66231C43.6264 4.66231 43.1481 5.28821 43.1481 6.59048V11.9512C43.1481 13.2535 43.6264 13.8962 44.6595 13.8962C45.6924 13.8962 46.1709 13.2535 46.1709 11.9512V9.17788Z\"/\u003e\u003cpath d=\"M32.492 10.1419C32.492 12.6954 34.1182 14.0484 37.0451 14.0484C39.9723 14.0484 41.5985 12.6954 41.5985 10.1419V6.59049C41.5985 5.28821 41.1394 4.66232 40.1061 4.66232C39.0732 4.66232 38.5948 5.28821 38.5948 6.59049V9.60062C38.5948 10.8521 38.2696 11.5455 37.0451 11.5455C35.8209 11.5455 35.4954 10.8521 35.4954 9.60062V6.59049C35.4954 5.28821 35.0173 4.66232 34.0034 4.66232C32.9703 4.66232 32.492 5.28821 32.492 6.59049V10.1419Z\" /\u003e\u003cpath fill-rule=\"evenodd\" clip-rule=\"evenodd\" d=\"M25.6622 17.6335C27.8049 17.6335 29.3739 16.9402 30.2537 15.6379C30.8468 14.7755 30.9615 13.5579 30.9615 11.9512V6.59049C30.9615 5.28821 30.4833 4.66231 29.4502 4.66231C28.9913 4.66231 28.4555 4.94978 28.1109 5.50789C27.499 4.86533 26.7335 4.56087 25.7005 4.56087C23.1369 4.56087 21.0134 6.57349 21.0134 9.27932C21.0134 11.9852 23.003 13.913 25.3754 13.913C26.5612 13.913 27.4607 13.4902 28.1109 12.6616C28.1109 12.7229 28.1161 12.7799 28.121 12.8346C28.1256 12.8854 28.1301 12.9342 28.1301 12.983C28.1301 14.4373 27.2502 15.2321 25.777 15.2321C24.8349 15.2321 24.1352 14.9821 23.5661 14.7787C23.176 14.6393 22.8472 14.5218 22.5437 14.5218C21.7977 14.5218 21.2429 15.0123 21.2429 15.6887C21.2429 16.7375 22.9072 17.6335 25.6622 17.6335ZM24.1317 9.27932C24.1317 7.94324 24.9928 7.09766 26.1024 7.09766C27.2119 7.09766 28.0918 7.94324 28.0918 9.27932C28.0918 10.6321 27.2311 11.5116 26.1024 11.5116C24.9737 11.5116 24.1317 10.6491 24.1317 9.27932Z\"/\u003e\u003cpath d=\"M16.8045 11.9512C16.8045 13.2535 17.2637 13.8962 18.2965 13.8962C19.3298 13.8962 19.8079 13.2535 19.8079 11.9512V8.12928C19.8079 5.82936 18.4879 4.62866 16.4027 4.62866C15.1594 4.62866 14.279 4.98375 13.3609 5.88013C12.653 5.05154 11.6581 4.62866 10.3573 4.62866C9.34336 4.62866 8.57809 4.89931 7.9466 5.5079C7.58314 4.9328 7.10506 4.66232 6.51203 4.66232C5.47873 4.66232 5.00066 5.28821 5.00066 6.59049V11.9512C5.00066 13.2535 5.47873 13.8962 6.51203 13.8962C7.54479 13.8962 8.0232 13.2535 8.0232 11.9512V8.90741C8.0232 7.58817 8.44431 6.91179 9.53458 6.91179C10.5104 6.91179 10.893 7.58817 10.893 8.94108V11.9512C10.893 13.2535 11.3711 13.8962 12.4044 13.8962C13.4375 13.8962 13.9157 13.2535 13.9157 11.9512V8.90741C13.9157 7.58817 14.3365 6.91179 15.4269 6.91179C16.4027 6.91179 16.8045 7.58817 16.8045 8.94108V11.9512Z\"/\u003e\u003cpath d=\"M3.31675 6.59049C3.31675 5.28821 2.83866 4.66232 1.82471 4.66232C0.791758 4.66232 0.313354 5.28821 0.313354 6.59049V11.9512C0.313354 13.2535 0.791758 13.8962 1.82471 13.8962C2.85798 13.8962 3.31675 13.2535 3.31675 11.9512V6.59049Z\" /\u003e\u003cpath d=\"M1.87209 0.400291C0.843612 0.400291 0 1.1159 0 1.98861C0 2.87869 0.822846 3.57676 1.87209 3.57676C2.90056 3.57676 3.7234 2.87869 3.7234 1.98861C3.7234 1.1159 2.90056 0.400291 1.87209 0.400291Z\" fill=\"#1BB76E\"/\u003e\u003c/svg\u003e\u003c/a\u003e",
                    contentPolicyHtml: "User contributions licensed under \u003ca href=\"https://stackoverflow.com/help/licensing\"\u003ecc by-sa\u003c/a\u003e \u003ca href=\"https://stackoverflow.com/legal/content-policy\"\u003e(content policy)\u003c/a\u003e",
                    allowUrls: true
                },
                onDemand: true,
                discardSelector: ".discard-answer"
                ,immediatelyShowMarkdownHelp:true
            });
                    }
    });
</script>
<div id="post-editor" class="post-editor js-post-editor">

    <div class="ps-relative">
        <div class="wmd-container mb8">
            <div id="wmd-button-bar" class="wmd-button-bar btr-sm"><ul id="wmd-button-row" class="wmd-button-row"><li id="wmd-bold-button" class="wmd-button" style="left: 0px;"><span style="background-position: 0px -20px;"></span></li><li id="wmd-italic-button" class="wmd-button" style="left: 25px;"><span style="background-position: -20px -20px;"></span></li><li id="wmd-spacer1" class="wmd-spacer" style="left: 50px;"><span style="background-position: -40px -20px;"></span></li><li id="wmd-link-button" class="wmd-button" style="left: 75px;"><span style="background-position: -40px -20px;"></span></li><li id="wmd-quote-button" class="wmd-button" style="left: 100px;"><span style="background-position: -60px -20px;"></span></li><li id="wmd-code-button" class="wmd-button" style="left: 125px;"><span style="background-position: -80px -20px;"></span></li><li id="wmd-image-button" class="wmd-button" style="left: 150px;"><span style="background-position: -100px -20px;"></span></li><li id="wmd-spacer2" class="wmd-spacer" style="left: 175px;"><span style="background-position: -120px -20px;"></span></li><li id="wmd-olist-button" class="wmd-button" style="left: 200px;"><span style="background-position: -120px -20px;"></span></li><li id="wmd-ulist-button" class="wmd-button" style="left: 225px;"><span style="background-position: -140px -20px;"></span></li><li id="wmd-heading-button" class="wmd-button" style="left: 250px;"><span style="background-position: -160px -20px;"></span></li><li id="wmd-hr-button" class="wmd-button" style="left: 275px;"><span style="background-position: -180px -20px;"></span></li><li id="wmd-spacer3" class="wmd-spacer" style="left: 300px;"><span style="background-position: -200px -20px;"></span></li><li id="wmd-undo-button" class="wmd-button" style="left: 325px;"><span style="background-position: -200px -20px;"></span></li><li id="wmd-redo-button" class="wmd-button" style="left: 350px;"><span style="background-position: -220px -20px;"></span></li><li class="wmd-spacer wmd-spacer-max"></li></ul></div>
            <div class="js-stacks-validation">
                <div class="ps-relative">
                    <textarea id="wmd-input" name="post-text" class="wmd-input s-input bar0 js-post-body-field" data-post-type-id="2" cols="92" rows="15" tabindex="101" data-min-length=""></textarea>
                </div>
                <div class="s-input-message mt4 d-none js-stacks-validation-message"></div>
            </div>
        </div>
    </div>

    <aside class="grid ai-start jc-space-between js-answer-help s-notice s-notice__warning pb0 pr4 pt4 mb8 d-none" role="status" aria-hidden="true">
    <div class="grid--cell pt8">
        <p>Thanks for contributing an answer to Stack Overflow!</p><ul><li>Please be sure to <em>answer the question</em>. Provide details and share your research!</li></ul><p>But <em>avoid</em> …</p><ul><li>Asking for help, clarification, or responding to other answers.</li><li>Making statements based on opinion; back them up with references or personal experience.</li></ul><p>To learn more, see our <a href="https://stackoverflow.com/help/how-to-answer">tips on writing great answers</a>.</p>
    </div>
    <button class="grid--cell js-answer-help-close-btn s-btn s-btn__muted fc-dark">
        <svg aria-hidden="true" class="svg-icon iconClear" width="18" height="18" viewBox="0 0 18 18"><path d="M15 4.41L13.59 3 9 7.59 4.41 3 3 4.41 7.59 9 3 13.59 4.41 15 9 10.41 13.59 15 15 13.59 10.41 9 15 4.41z"></path></svg>
    </button>
</aside>


    <div id="draft-saved" class="fc-success float-left h24" style="display:none;">Draft saved</div>
    <div id="draft-discarded" class="fc-error float-left h24" style="display:none;">Draft discarded</div>



        <div id="wmd-preview" class="s-prose wmd-preview js-wmd-preview"></div>
        <div></div>
        <div class="edit-block">
            <input id="fkey" name="fkey" type="hidden" value="06f4a5ec10401c8de359874849bfe5f8510ad6928c6d18bc248daae27aa762fb">
            <input id="author" name="author" type="text">
        </div>

</div>


                                <div class="ps-relative">
                                                <div class="form-item new-post-login p0 my16">
                <div class="grid gs16 md:fd-column new-login-form">
                    <div class="grid fd-column w50 md:w-auto gsy gs8 jc-space-between new-login-left">
                        <h3 class="grid--cell fs-title">Sign up or <a id="login-link" href="https://stackoverflow.com/users/login?ssrc=question_page&amp;returnurl=https%3a%2f%2fstackoverflow.com%2fquestions%2f48301186%2fcropping-concave-polygon-from-image-using-opencv-python%23new-answer">log in</a></h3>
                        <script>
                            StackExchange.ready(function () {
                                StackExchange.helpers.onClickDraftSave('#login-link');
                            });
                        </script>
                        <div class="grid--cell s-btn s-btn__muted s-btn__outlined s-btn__icon google-login" data-ga="[&quot;sign up&quot;,&quot;Sign Up Started - Google&quot;,&quot;New Post&quot;,null,null]">
                            <svg aria-hidden="true" class="native svg-icon iconGoogle" width="18" height="18" viewBox="0 0 18 18"><path d="M16.51 8H8.98v3h4.3c-.18 1-.74 1.48-1.6 2.04v2.01h2.6a7.8 7.8 0 002.38-5.88c0-.57-.05-.66-.15-1.18z" fill="#4285F4"></path><path d="M8.98 17c2.16 0 3.97-.72 5.3-1.94l-2.6-2a4.8 4.8 0 01-7.18-2.54H1.83v2.07A8 8 0 008.98 17z" fill="#34A853"></path><path d="M4.5 10.52a4.8 4.8 0 010-3.04V5.41H1.83a8 8 0 000 7.18l2.67-2.07z" fill="#FBBC05"></path><path d="M8.98 4.18c1.17 0 2.23.4 3.06 1.2l2.3-2.3A8 8 0 001.83 5.4L4.5 7.49a4.77 4.77 0 014.48-3.3z" fill="#EA4335"></path></svg> Sign up using Google
                        </div>
                        <div class="grid--cell s-btn s-btn__muted s-btn__icon facebook-login" data-ga="[&quot;sign up&quot;,&quot;Sign Up Started - Facebook&quot;,&quot;New Post&quot;,null,null]">
                            <svg aria-hidden="true" class="svg-icon iconFacebook" width="18" height="18" viewBox="0 0 18 18"><path d="M3 1a2 2 0 00-2 2v12c0 1.1.9 2 2 2h12a2 2 0 002-2V3a2 2 0 00-2-2H3zm6.55 16v-6.2H7.46V8.4h2.09V6.61c0-2.07 1.26-3.2 3.1-3.2.88 0 1.64.07 1.87.1v2.16h-1.29c-1 0-1.19.48-1.19 1.18V8.4h2.39l-.31 2.42h-2.08V17h-2.5z" fill="#4167B2"></path></svg> Sign up using Facebook
                        </div>
                        <div class="grid--cell s-btn s-btn__muted s-btn__outlined s-btn__icon stackexchange-login" data-ga="[&quot;sign up&quot;,&quot;Sign Up Navigation&quot;,&quot;New Post&quot;,null,null]">
                            <svg aria-hidden="true" class="native svg-icon iconLogoGlyphXSm" width="18" height="18" viewBox="0 0 18 18"><path d="M14 16v-5h2v7H2v-7h2v5h10z" fill="#BCBBBB"></path><path d="M12.09.72l-1.21.9 4.5 6.07 1.22-.9L12.09.71zM5 15h8v-2H5v2zm9.15-5.87L8.35 4.3l.96-1.16 5.8 4.83-.96 1.16zm-7.7-1.47l6.85 3.19.63-1.37-6.85-3.2-.63 1.38zm6.53 5L5.4 11.39l.38-1.67 7.42 1.48-.22 1.46z" fill="#F48024"></path></svg> Sign up using Email and Password
                        </div>
                    </div>
                    <input type="hidden" name="use-facebook" class="use-facebook" value="false">
                    <input type="hidden" name="use-google" class="use-google" value="false">
                    <button type="button" class="d-none js-submit-openid">Submit</button>
                    <div class="grid gsy gs8 fd-column w50 md:w-auto new-login-right form-item p0">
                                <h3 class="grid--cell fs-title">Post as a guest</h3>
            <div class="grid--cell">
                <div class="grid gs4 gsy fd-column">
                    <label class="s-label" for="display-name">Name</label>
                    <div class="grid ps-relative">
                        <input class="s-input" id="display-name" name="display-name" maxlength="30" type="text" value="" tabindex="105" placeholder="">
                    </div>
                </div>
            </div>
            <div class="grid--cell">
                <div class="grid gs4 gsy fd-column">
                    <div class="grid--cell">
                        <div class="grid gs2 gsy fd-column">
                            <label class="grid--cell s-label" for="m-address">Email</label>
                            <p class="grid--cell s-description">Required, but never shown</p>
                        </div>
                    </div>
                    <div class="grid ps-relative">
                        <input class="s-input js-post-email-field" id="m-address" name="m-address" type="text" value="" size="40" tabindex="106" placeholder="">
                    </div>
                </div>
            </div>

                    </div>
                </div>
            </div>
            <script>
                StackExchange.ready(
                    function () {
                        StackExchange.openid.initPostLogin('.new-post-login', 'https%3a%2f%2fstackoverflow.com%2fquestions%2f48301186%2fcropping-concave-polygon-from-image-using-opencv-python%23new-answer', 'question_page');
                    }
                );
            </script>
            <noscript>
                        <h3 class="grid--cell fs-title">Post as a guest</h3>
            <div class="grid--cell">
                <div class="grid gs4 gsy fd-column">
                    <label class="s-label" for="display-name">Name</label>
                    <div class="grid ps-relative">
                        <input class="s-input" id="display-name" name="display-name" maxlength="30" type="text" value="" tabindex="105" placeholder="" />
                    </div>
                </div>
            </div>
            <div class="grid--cell">
                <div class="grid gs4 gsy fd-column">
                    <div class="grid--cell">
                        <div class="grid gs2 gsy fd-column">
                            <label class="grid--cell s-label" for="m-address">Email</label>
                            <p class="grid--cell s-description">Required, but never shown</p>
                        </div>
                    </div>
                    <div class="grid ps-relative">
                        <input class="s-input js-post-email-field" id="m-address" name="m-address" type="text" value="" size="40" tabindex="106" placeholder="" />
                    </div>
                </div>
            </div>

            </noscript>

                                </div>

                                    <div class="form-submit cbt grid gsx gs4">
                                        <button id="submit-button" class="grid--cell s-btn s-btn__primary s-btn__icon" type="submit" tabindex="120" autocomplete="off">
Post Your Answer                                        </button>
                                        <button class="grid--cell s-btn s-btn__danger discard-answer dno">
                                            Discard
                                        </button>
                                            <p class="privacy-policy-agreement">
                                                By clicking “Post Your Answer”, you agree to our <a href="https://stackoverflow.com/legal/terms-of-service/public" name="tos" target="_blank" class="-link">terms of service</a>, <a href="https://stackoverflow.com/legal/privacy-policy" name="privacy" target="_blank" class="-link">privacy policy</a> and <a href="https://stackoverflow.com/legal/cookie-policy" name="cookie" target="_blank" class="-link">cookie policy</a><input type="hidden" name="legalLinksShown" value="1">
                                            </p>
                                    </div>
                                    <div class="js-general-error general-error cbt d-none"></div>
                            </form>



                            <h2 class="bottom-notice" data-loc="1">
Not the answer you're looking for? Browse other questions tagged <a href="https://stackoverflow.com/questions/tagged/python" class="post-tag" title="show questions tagged &#39;python&#39;" rel="tag">python</a> <a href="https://stackoverflow.com/questions/tagged/opencv" class="post-tag" title="show questions tagged &#39;opencv&#39;" rel="tag">opencv</a> <a href="https://stackoverflow.com/questions/tagged/image-processing" class="post-tag" title="show questions tagged &#39;image-processing&#39;" rel="tag">image-processing</a> <a href="https://stackoverflow.com/questions/tagged/crop" class="post-tag" title="show questions tagged &#39;crop&#39;" rel="tag">crop</a>  or <a href="https://stackoverflow.com/questions/ask">ask your own question</a>.                            </h2>
                </div>
            </div>
            <div id="sidebar" class="show-votes" role="complementary" aria-label="sidebar">
                
<div class="s-sidebarwidget s-sidebarwidget__yellow s-anchors s-anchors__grayscale mb16" data-tracker="cb=1">
    <ul class="d-block p0 m0">
                    <div class="s-sidebarwidget--header s-sidebarwidget__small-bold-text fc-light d:fc-black-900 bb bbw1">
                        The Overflow Blog
                    </div>
        <li class="s-sidebarwidget--item grid px16">
            <div class="grid--cell1 fl-shrink0">
<svg aria-hidden="true" class="va-text-top svg-icon iconPencilSm" width="14" height="14" viewBox="0 0 14 14"><path d="M11.1 1.71l1.13 1.12c.2.2.2.51 0 .71L11.1 4.7 9.21 2.86l1.17-1.15c.2-.2.51-.2.71 0zM2 10.12l6.37-6.43 1.88 1.88L3.88 12H2v-1.88z"></path></svg>            </div>
            <div class="grid--cell">
                <a href="https://stackoverflow.blog/2020/09/02/if-everyone-hates-it-why-is-oop-still-so-widely-spread/?cb=1" class="js-gps-track" data-ga="[&quot;community bulletin board&quot;,&quot;The Overflow Blog&quot;,&quot;https://stackoverflow.blog/2020/09/02/if-everyone-hates-it-why-is-oop-still-so-widely-spread/&quot;,null,null]" data-gps-track="communitybulletin.click({ priority: 1, position: 0 })">If everyone hates it, why is OOP still so widely spread?</a>
            </div>
        </li>
        <li class="s-sidebarwidget--item grid px16">
            <div class="grid--cell1 fl-shrink0">
<svg aria-hidden="true" class="va-text-top svg-icon iconPencilSm" width="14" height="14" viewBox="0 0 14 14"><path d="M11.1 1.71l1.13 1.12c.2.2.2.51 0 .71L11.1 4.7 9.21 2.86l1.17-1.15c.2-.2.51-.2.71 0zM2 10.12l6.37-6.43 1.88 1.88L3.88 12H2v-1.88z"></path></svg>            </div>
            <div class="grid--cell">
                <a href="https://stackoverflow.blog/2020/09/04/podcast-266-ok-who-vandalized-wikipedia/?cb=1" class="js-gps-track" data-ga="[&quot;community bulletin board&quot;,&quot;The Overflow Blog&quot;,&quot;https://stackoverflow.blog/2020/09/04/podcast-266-ok-who-vandalized-wikipedia/&quot;,null,null]" data-gps-track="communitybulletin.click({ priority: 1, position: 1 })">Podcast 266: Ok, who vandalized Wikipedia?</a>
            </div>
        </li>
                    <div class="s-sidebarwidget--header s-sidebarwidget__small-bold-text fc-light d:fc-black-900 bb bbw1">
                        Featured on Meta
                    </div>
        <li class="s-sidebarwidget--item grid px16">
            <div class="grid--cell1 fl-shrink0">
<div class="favicon favicon-stackexchangemeta" title="Meta Stack Exchange"></div>            </div>
            <div class="grid--cell">
                <a href="https://meta.stackexchange.com/questions/353446/new-post-formatting?cb=1" class="js-gps-track" data-ga="[&quot;community bulletin board&quot;,&quot;Featured on Meta&quot;,&quot;https://meta.stackexchange.com/questions/353446/new-post-formatting&quot;,null,null]" data-gps-track="communitybulletin.click({ priority: 3, position: 2 })">New post formatting</a>
            </div>
        </li>
        <li class="s-sidebarwidget--item grid px16">
            <div class="grid--cell1 fl-shrink0">
<div class="favicon favicon-stackexchangemeta" title="Meta Stack Exchange"></div>            </div>
            <div class="grid--cell">
                <a href="https://meta.stackexchange.com/questions/353492/hot-meta-posts-allow-for-removal-by-moderators-and-thoughts-about-future-impro?cb=1" class="js-gps-track" title="Hot Meta Posts: Allow for removal by moderators, and thoughts about future improvements" data-ga="[&quot;community bulletin board&quot;,&quot;Featured on Meta&quot;,&quot;https://meta.stackexchange.com/questions/353492/hot-meta-posts-allow-for-removal-by-moderators-and-thoughts-about-future-impro&quot;,null,null]" data-gps-track="communitybulletin.click({ priority: 3, position: 3 })">Hot Meta Posts: Allow for removal by moderators, and thoughts about future…</a>
            </div>
        </li>
        <li class="s-sidebarwidget--item grid px16">
            <div class="grid--cell1 fl-shrink0">
<div class="favicon favicon-stackoverflowmeta" title="Meta Stack Overflow"></div>            </div>
            <div class="grid--cell">
                <a href="https://meta.stackoverflow.com/questions/400801/new-features-on-stack-overflow-jobs-company-updates-follow-and-ads?cb=1" class="js-gps-track" data-ga="[&quot;community bulletin board&quot;,&quot;Featured on Meta&quot;,&quot;https://meta.stackoverflow.com/questions/400801/new-features-on-stack-overflow-jobs-company-updates-follow-and-ads&quot;,null,null]" data-gps-track="communitybulletin.click({ priority: 6, position: 4 })">New Features on Stack Overflow Jobs: Company Updates, Follow, and Ads</a>
            </div>
        </li>
        <li class="s-sidebarwidget--item grid px16">
            <div class="grid--cell1 fl-shrink0">
<div class="favicon favicon-stackoverflowmeta" title="Meta Stack Overflow"></div>            </div>
            <div class="grid--cell">
                <a href="https://meta.stackoverflow.com/questions/295650/how-does-the-triage-review-queue-work?cb=1" class="js-gps-track" data-ga="[&quot;community bulletin board&quot;,&quot;Featured on Meta&quot;,&quot;https://meta.stackoverflow.com/questions/295650/how-does-the-triage-review-queue-work&quot;,null,null]" data-gps-track="communitybulletin.click({ priority: 6, position: 5 })">How does the Triage review queue work?</a>
            </div>
        </li>
    </ul>
</div>


                    <div class="js-sidebar-zone" style="">
                        <div class="js-zone-container zone-container-sidebar">
    <div id="dfp-tsb" class="everyonelovesstackoverflow everyoneloves__top-sidebar" data-dfp-zone="true" data-google-query-id="CIXh48Kwz-sCFUKbSwUdfMQJHQ" data-clc-ready="true" style="min-height: auto; height: auto; display: none;"><div id="google_ads_iframe_/248424177/stackoverflow.com/sb/question-pages_0__container__" style="border: 0pt none; width: 300px; height: auto; min-height: auto; display: none;"></div></div>
    <div class="js-report-ad-button-container " style="width: 300px"></div>
</div>

                        <div class="js-zone-container zone-container-sidebar">
    <div id="dfp-msb" class="everyonelovesstackoverflow everyoneloves__mid-sidebar" data-dfp-zone="true" data-google-query-id="CLD148Kwz-sCFXaESwUdpdQBXw" data-clc-ready="true" style="min-height: auto; height: auto; display: none;"><div id="google_ads_iframe_/248424177/stackoverflow.com/msb/question-pages_0__container__" style="border: 0pt none; display: none; width: 300px; height: auto; min-height: auto;"><iframe frameborder="0" src="./none_files/container(1).html" id="google_ads_iframe_/248424177/stackoverflow.com/msb/question-pages_0" title="3rd party ad content" name="" scrolling="no" marginwidth="0" marginheight="0" width="300" height="250" data-is-safeframe="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-top-navigation-by-user-activation" data-google-container-id="3" style="border: 0px; vertical-align: bottom; min-height: auto; height: auto; display: none;" data-load-complete="true"></iframe></div></div>
    <div class="js-report-ad-button-container " style="width: 300px"></div>
</div>

                        <div id="hireme" class="check-out-purple tex2jax_ignore clc-cp-multi"><a class="header grid " href="https://stackoverflow.com/jobs/companies?so_medium=Ad&amp;so_source=SharedCompanyAd&amp;so_campaign=GenericPurple" target="_blank" data-clc-click="https://clc.stackoverflow.com/click?an=4yp9lOF9JOCGB-vDXj9PJiaWps4W8WyWrevE_06Vv92mwWDE0LOBgaHBnpGRgYWb9cxt8Yk35L-eQIhzs954Ij7_oXzzJWSxdQ_FP9-Vv34OWezNbfGNN-SnnkSIMSTWlTwTtr-TyaUHAA&amp;cr=656219&amp;ct=1&amp;url=https%3A%2F%2Fstackoverflow.com%2Fjobs%2Fcompanies%3Fso_medium%3DAd%26so_source%3DSharedCompanyAd%26so_campaign%3DGenericPurple%26med%3Dclc%26clc-var%3D50&amp;sig=rUe3tAVOZUsAlw"><span class="grid--cell fl1">Check out these <strong>companies</strong></span></a><div class="middle"><ul class="companies pt6"><li class="clc-dismissable"><div class="company-wrap grid"><div class="grid--cell fl-shrink0"><img class="mr8 w32 h32 bar-sm" src="./none_files/cI8cI.png"></div><a class="company grid--cell fl1" title="Ringba. Click to learn more." href="https://stackoverflow.com/jobs/companies/ringba?so_medium=Ad&amp;so_source=SharedCompanyAd&amp;so_campaign=GenericPurple" target="_blank" data-clc-click="https://clc.stackoverflow.com/click?an=4yp9lOF9JOCGB-vDXj9PJiaWps4W8WyWrevE_06Vv92mwWDE0LOBgaHBnpGRgYWb9cxt8Yk35L-eQIhzs954Ij7_oXzzJWSxdQ_FP9-Vv34OWezNbfGNN-SnnkSIMSTWlTwTtr-TyaUHAA&amp;cr=664693&amp;ct=0&amp;url=https%3A%2F%2Fstackoverflow.com%2Fjobs%2Fcompanies%2Fringba%3Fso_medium%3DAd%26so_source%3DSharedCompanyAd%26so_campaign%3DGenericPurple%26med%3Dclc%26clc-var%3D50&amp;sig=Ds7UqapgH6_9pw"><div class="title">Ringba</div><div class="industries v-truncate2">Ad Tech, SaaS, Telecommunications</div><div><span class="s-tag mr2">javascript</span><span class="s-tag mr2">.net</span><span class="s-tag">amazon-web-services</span></div></a></div><a class="clc-dismiss grid--cell" data-clc-click="https://clc.stackoverflow.com/click?an=4yp9lOF9JOCGB-vDXj9PJiaWps4W8WyWrevE_06Vv92mwWDE0LOBgaHBnpGRgYWb9cxt8Yk35L-eQIhzs954Ij7_oXzzJWSxdQ_FP9-Vv34OWezNbfGNN-SnnkSIMSTWlTwTtr-TyaUHAA&amp;cr=664693&amp;ct=-3&amp;sig=lmL5S9MfobLrcQ" data-clc-meta-target="-3"><svg viewBox="0 0 13.6 13.6"><path d="M11.4 2.3C8.9-.2 4.8-.2 2.3 2.3s-2.5 6.6 0 9.1 6.6 2.5 9.1 0 2.5-6.6 0-9.1zM8.6 9.5L6.8 7.7 5 9.5l-.9-.9 1.8-1.8L4.1 5l.9-.9 1.8 1.8 1.8-1.8.9.9-1.8 1.8 1.8 1.8-.9.9z"></path></svg><span class="clc-tooltip above-left">dismiss this company</span></a></li><li class="clc-dismissable"><div class="company-wrap grid"><div class="grid--cell fl-shrink0"><img class="mr8 w32 h32 bar-sm" src="./none_files/kRD2f.jpg"></div><a class="company grid--cell fl1" title="The Art of Education University. Click to learn more." href="https://stackoverflow.com/jobs/companies/the-art-of-education-university?so_medium=Ad&amp;so_source=SharedCompanyAd&amp;so_campaign=GenericPurple" target="_blank" data-clc-click="https://clc.stackoverflow.com/click?an=4yp9lOF9JOCGB-vDXj9PJiaWps4W8WyWrevE_06Vv92mwWDE0LOBgaHBnpGRgYWb9cxt8Yk35L-eQIhzs954Ij7_oXzzJWSxdQ_FP9-Vv34OWezNbfGNN-SnnkSIMSTWlTwTtr-TyaUHAA&amp;cr=665859&amp;ct=0&amp;url=https%3A%2F%2Fstackoverflow.com%2Fjobs%2Fcompanies%2Fthe-art-of-education-university%3Fso_medium%3DAd%26so_source%3DSharedCompanyAd%26so_campaign%3DGenericPurple%26med%3Dclc%26clc-var%3D50&amp;sig=ZaWEB2zolumMMA"><div class="title">The Art of Education University</div><div class="industries v-truncate2">Higher Education</div><div><span class="s-tag mr2">python</span><span class="s-tag mr2">javascript</span><span class="s-tag">html</span></div></a></div><a class="clc-dismiss grid--cell" data-clc-click="https://clc.stackoverflow.com/click?an=4yp9lOF9JOCGB-vDXj9PJiaWps4W8WyWrevE_06Vv92mwWDE0LOBgaHBnpGRgYWb9cxt8Yk35L-eQIhzs954Ij7_oXzzJWSxdQ_FP9-Vv34OWezNbfGNN-SnnkSIMSTWlTwTtr-TyaUHAA&amp;cr=665859&amp;ct=-3&amp;sig=GiNWnwMtLn6adA" data-clc-meta-target="-3"><svg viewBox="0 0 13.6 13.6"><path d="M11.4 2.3C8.9-.2 4.8-.2 2.3 2.3s-2.5 6.6 0 9.1 6.6 2.5 9.1 0 2.5-6.6 0-9.1zM8.6 9.5L6.8 7.7 5 9.5l-.9-.9 1.8-1.8L4.1 5l.9-.9 1.8 1.8 1.8-1.8.9.9-1.8 1.8 1.8 1.8-.9.9z"></path></svg><span class="clc-tooltip above-left">dismiss this company</span></a></li><li class="clc-dismissable"><div class="company-wrap grid"><div class="grid--cell fl-shrink0"><img class="mr8 w32 h32 bar-sm" src="./none_files/il9Yp.png"></div><a class="company grid--cell fl1" title="CynLr. Click to learn more." href="https://stackoverflow.com/jobs/companies/cynlr?so_medium=Ad&amp;so_source=SharedCompanyAd&amp;so_campaign=GenericPurple" target="_blank" data-clc-click="https://clc.stackoverflow.com/click?an=4yp9lOF9JOCGB-vDXj9PJiaWps4W8WyWrevE_06Vv92mwWDE0LOBgaHBnpGRgYWb9cxt8Yk35L-eQIhzs954Ij7_oXzzJWSxdQ_FP9-Vv34OWezNbfGNN-SnnkSIMSTWlTwTtr-TyaUHAA&amp;cr=665431&amp;ct=0&amp;url=https%3A%2F%2Fstackoverflow.com%2Fjobs%2Fcompanies%2Fcynlr%3Fso_medium%3DAd%26so_source%3DSharedCompanyAd%26so_campaign%3DGenericPurple%26med%3Dclc%26clc-var%3D50&amp;sig=2mdXml7i4qcPiw"><div class="title">CynLr</div><div class="industries v-truncate2">AI Research, Computer Vision, Robotics</div><div><span class="s-tag mr2">image-processing</span><span class="s-tag mr2">c++</span><span class="s-tag">computer-vision</span></div><div class="extra-info"><span>1 open job</span></div></a></div><a class="clc-dismiss grid--cell" data-clc-click="https://clc.stackoverflow.com/click?an=4yp9lOF9JOCGB-vDXj9PJiaWps4W8WyWrevE_06Vv92mwWDE0LOBgaHBnpGRgYWb9cxt8Yk35L-eQIhzs954Ij7_oXzzJWSxdQ_FP9-Vv34OWezNbfGNN-SnnkSIMSTWlTwTtr-TyaUHAA&amp;cr=665431&amp;ct=-3&amp;sig=smroMpPqtdvGpQ" data-clc-meta-target="-3"><svg viewBox="0 0 13.6 13.6"><path d="M11.4 2.3C8.9-.2 4.8-.2 2.3 2.3s-2.5 6.6 0 9.1 6.6 2.5 9.1 0 2.5-6.6 0-9.1zM8.6 9.5L6.8 7.7 5 9.5l-.9-.9 1.8-1.8L4.1 5l.9-.9 1.8 1.8 1.8-1.8.9.9-1.8 1.8 1.8 1.8-.9.9z"></path></svg><span class="clc-tooltip above-left">dismiss this company</span></a></li><li class="clc-dismissable"><div class="company-wrap grid"><div class="grid--cell fl-shrink0"><img class="mr8 w32 h32 bar-sm" src="./none_files/OBeOl.png"></div><a class="company grid--cell fl1" title="Apple. Click to learn more." href="https://stackoverflow.com/jobs/companies/apple?so_medium=Ad&amp;so_source=SharedCompanyAd&amp;so_campaign=GenericPurple" target="_blank" data-clc-click="https://clc.stackoverflow.com/click?an=4yp9lOF9JOCGB-vDXj9PJiaWps4W8WyWrevE_06Vv92mwWDE0LOBgaHBnpGRgYWb9cxt8Yk35L-eQIhzs954Ij7_oXzzJWSxdQ_FP9-Vv34OWezNbfGNN-SnnkSIMSTWlTwTtr-TyaUHAA&amp;cr=664725&amp;ct=0&amp;url=https%3A%2F%2Fstackoverflow.com%2Fjobs%2Fcompanies%2Fapple%3Fso_medium%3DAd%26so_source%3DSharedCompanyAd%26so_campaign%3DGenericPurple%26med%3Dclc%26clc-var%3D50&amp;sig=pIME3BAI1ylcbg"><div class="title">Apple</div><div class="industries v-truncate2">Consumer Electronics</div><div><span class="s-tag mr2">python</span><span class="s-tag mr2">machine-learning</span><span class="s-tag">c++</span></div><div class="extra-info"><span>150 open jobs<strong> · </strong>1 follower</span></div></a></div><a class="clc-dismiss grid--cell" data-clc-click="https://clc.stackoverflow.com/click?an=4yp9lOF9JOCGB-vDXj9PJiaWps4W8WyWrevE_06Vv92mwWDE0LOBgaHBnpGRgYWb9cxt8Yk35L-eQIhzs954Ij7_oXzzJWSxdQ_FP9-Vv34OWezNbfGNN-SnnkSIMSTWlTwTtr-TyaUHAA&amp;cr=664725&amp;ct=-3&amp;sig=CYynl76UXj5eGA" data-clc-meta-target="-3"><svg viewBox="0 0 13.6 13.6"><path d="M11.4 2.3C8.9-.2 4.8-.2 2.3 2.3s-2.5 6.6 0 9.1 6.6 2.5 9.1 0 2.5-6.6 0-9.1zM8.6 9.5L6.8 7.7 5 9.5l-.9-.9 1.8-1.8L4.1 5l.9-.9 1.8 1.8 1.8-1.8.9.9-1.8 1.8 1.8 1.8-.9.9z"></path></svg><span class="clc-tooltip above-left">dismiss this company</span></a></li></ul><a class="footer" href="https://stackoverflow.com/jobs/companies?so_medium=Ad&amp;so_source=SharedCompanyAd&amp;so_campaign=GenericPurple" target="_blank" data-clc-click="https://clc.stackoverflow.com/click?an=4yp9lOF9JOCGB-vDXj9PJiaWps4W8WyWrevE_06Vv92mwWDE0LOBgaHBnpGRgYWb9cxt8Yk35L-eQIhzs954Ij7_oXzzJWSxdQ_FP9-Vv34OWezNbfGNN-SnnkSIMSTWlTwTtr-TyaUHAA&amp;cr=656219&amp;ct=2&amp;url=https%3A%2F%2Fstackoverflow.com%2Fjobs%2Fcompanies%3Fso_medium%3DAd%26so_source%3DSharedCompanyAd%26so_campaign%3DGenericPurple%26med%3Dclc%26clc-var%3D50&amp;sig=pbVa3N_YHZlhWQ"><div class="grid ai-baseline pl12 pb12 pr12 pt6"><div class="grid--cell"><svg aria-hidden="true" class="svg-icon iconLogoGlyphSm" width="19" height="22" viewBox="0 0 19 22"><g><path fill="#C1BEBC" d="M16 20v-6h2v8H0v-8h2v6z"></path><path d="M4 18h10v-2H4v2zm8.72-18l-1.57 1.17L17 9.05l1.57-1.18L12.72 0zM7.86 4.64l7.54 6.28 1.25-1.5-7.54-6.29-1.25 1.51zM5.39 9.01l8.9 4.14.83-1.78-8.9-4.14L5.4 9zm-1.27 4.6l9.91 1.67.13-1.67-9.63-1.92-.4 1.92z" fill="#F48024"></path></g></svg></div><div class="grid--cell fl1 pl8">More companies on <b>Stack Overflow</b></div><div class="grid--cell"><svg aria-hidden="true" class="svg-icon arrow-ico iconArrowRightAlt" width="18" height="18" viewBox="0 0 18 18"><path d="M6.41 2L5 3.41 10.59 9 5 14.59 6.41 16l7-7z"></path></svg></div></div></a></div><img src="./none_files/impression.gif" class="impression" style="display: none;"></div>
                    </div>
    
<div class="s-sidebarwidget mb16 module">
    <div class="s-sidebarwidget--header grid ai-center">
        <a href="https://chat.stackoverflow.com/" class="js-chat-ad-link" title="58 users active in 47 rooms the last 60 minutes">58 people chatting</a>
    </div>
        <div class="s-sidebarwidget--content s-sidebarwidget__items js-chat-ad-rooms"><div class="s-sidebarwidget--item"><div class="grid fd-column gs2"><a class="grid--cell" href="https://chat.stackoverflow.com/rooms/6">Python</a><div class="grid--cell fs-fine fc-black-300 mb4" title="2020-09-04 11:05:43Z">12 mins ago - <a href="https://chat.stackoverflow.com/users/8393101">Pherdindy</a></div><div class="grid gs4 ai-center fw-wrap"><a class="grid--cell" href="https://chat.stackoverflow.com/users/8393101"><img class="bar-sm" title="Pherdindy: 12 mins ago" src="./none_files/aMexg.jpg" width="23" height="23"></a><a class="grid--cell" href="https://chat.stackoverflow.com/users/146073"><img class="bar-sm" title="holdenweb: 1 hour ago" src="./none_files/2c69ccb9eb83c7ef2ba155a850df68a9.jpeg" width="23" height="23"></a><a class="grid--cell" href="https://chat.stackoverflow.com/users/5349916"><img class="bar-sm" title="MisterMiyagi: 2 hours ago" src="./none_files/QovYv.jpg" width="23" height="23"></a><a class="grid--cell" href="https://chat.stackoverflow.com/users/5067311"><img class="bar-sm" title="Andras Deak: 2 hours ago" src="./none_files/qjltV.png" width="23" height="23"></a><a class="grid--cell" href="https://chat.stackoverflow.com/users/13277690"><img class="bar-sm" title="Kwsswart: 3 hours ago" src="./none_files/5d3a763825c3d04322e8c5fe11af9cad" width="23" height="23"></a><a class="grid--cell" href="https://chat.stackoverflow.com/users/12465136"><img class="bar-sm" title="Aran-Fey: 16 hours ago" src="./none_files/s64JD.png" width="23" height="23"></a><a class="grid--cell" href="https://chat.stackoverflow.com/users/165216"><img class="bar-sm" title="PaulMcG: 17 hours ago" src="./none_files/eE7OR.jpg" width="23" height="23"></a></div></div></div><div class="s-sidebarwidget--item"><div class="grid fd-column gs2"><a class="grid--cell" href="https://chat.stackoverflow.com/rooms/219265">Data Science Discussions 5</a><div class="grid--cell fs-fine fc-black-300 mb4" title="2020-09-04 02:52:36Z">8 hours ago - <a href="https://chat.stackoverflow.com/users/13415013">nerd</a></div><div class="grid gs4 ai-center fw-wrap"></div></div></div></div>
</div>


    <script>
    // <!--
        StackExchange.ready(function () {
            var options = {
                chatUrl: 'https://chat.stackoverflow.com',
                reloadUrl: '/api/recent-chat',
                preloadedData: null,
                tagBased: true,
            };

            StackExchange.chatAd.init(options);
        });
    // -->
    </script>


<div class="module sidebar-linked">
	<h4 id="h-linked">Linked</h4>
	<div class="linked" data-tracker="lq=1">
            <div class="spacer js-gps-track" data-gps-track="linkedquestion.click({ source_post_id: 48301186, target_question_id: 54628147, position: 0 })">
				<a href="https://stackoverflow.com/q/54628147?lq=1" title="Vote score (upvotes - downvotes)">
					<div class="answer-votes  default">4</div>
				</a>
				<a href="https://stackoverflow.com/questions/54628147/how-to-detect-the-colors-of-detected-shapes-opencv?noredirect=1&amp;lq=1" class="question-hyperlink">How to detect the colors of detected shapes OpenCV</a>
			</div>
            <div class="spacer js-gps-track" data-gps-track="linkedquestion.click({ source_post_id: 48301186, target_question_id: 55212592, position: 1 })">
				<a href="https://stackoverflow.com/q/55212592?lq=1" title="Vote score (upvotes - downvotes)">
					<div class="answer-votes  default">0</div>
				</a>
				<a href="https://stackoverflow.com/questions/55212592/how-to-remove-multiple-polygons-using-opencv-python?noredirect=1&amp;lq=1" class="question-hyperlink">How to remove multiple polygons using Opencv python</a>
			</div>
            <div class="spacer js-gps-track" data-gps-track="linkedquestion.click({ source_post_id: 48301186, target_question_id: 52424043, position: 2 })">
				<a href="https://stackoverflow.com/q/52424043?lq=1" title="Vote score (upvotes - downvotes)">
					<div class="answer-votes  default">0</div>
				</a>
				<a href="https://stackoverflow.com/questions/52424043/python-2-7-cv2-rasterio-gets-an-error-numpy-ndarray-object-is-not-callable?noredirect=1&amp;lq=1" class="question-hyperlink">Python 2.7 - CV2, Rasterio gets an error numpy.ndarray object is not callable</a>
			</div>
            <div class="spacer js-gps-track" data-gps-track="linkedquestion.click({ source_post_id: 48301186, target_question_id: 61842824, position: 3 })">
				<a href="https://stackoverflow.com/q/61842824?lq=1" title="Vote score (upvotes - downvotes)">
					<div class="answer-votes  default">0</div>
				</a>
				<a href="https://stackoverflow.com/questions/61842824/what-is-the-difference-between-cropping-an-image-and-applying-an-roi-region-of?noredirect=1&amp;lq=1" class="question-hyperlink">What is the difference between cropping an image and applying an ROI (region of interest) on the image</a>
			</div>
            <div class="spacer js-gps-track" data-gps-track="linkedquestion.click({ source_post_id: 48301186, target_question_id: 63719908, position: 4 })">
				<a href="https://stackoverflow.com/q/63719908?lq=1" title="Vote score (upvotes - downvotes)">
					<div class="answer-votes  default">0</div>
				</a>
				<a href="https://stackoverflow.com/questions/63719908/cropping-a-polygon-and-add-a-color-background-in-python?noredirect=1&amp;lq=1" class="question-hyperlink">cropping a polygon and add a color background in python</a>
			</div>
	</div>
</div>

                    <div class="module sidebar-related">
                        <h4 id="h-related">Related</h4>
                        <div class="related js-gps-related-questions" data-tracker="rq=1">
                            <div class="spacer js-gps-track"><a href="https://stackoverflow.com/q/89228?rq=1" title="Vote score (upvotes - downvotes)"><div class="answer-votes answered-accepted extra-large">5002</div></a><a href="https://stackoverflow.com/questions/89228/how-to-call-an-external-command?rq=1" class="question-hyperlink">How to call an external command?</a></div><div class="spacer js-gps-track"><a href="https://stackoverflow.com/q/541390?rq=1" title="Vote score (upvotes - downvotes)"><div class="answer-votes answered-accepted extra-large">1348</div></a><a href="https://stackoverflow.com/questions/541390/extracting-extension-from-filename-in-python?rq=1" class="question-hyperlink">Extracting extension from filename in Python</a></div><div class="spacer js-gps-track"><a href="https://stackoverflow.com/q/3684484?rq=1" title="Vote score (upvotes - downvotes)"><div class="answer-votes answered-accepted large">881</div></a><a href="https://stackoverflow.com/questions/3684484/peak-detection-in-a-2d-array?rq=1" class="question-hyperlink">Peak detection in a 2D array</a></div><div class="spacer js-gps-track"><a href="https://stackoverflow.com/q/9371238?rq=1" title="Vote score (upvotes - downvotes)"><div class="answer-votes answered-accepted extra-large">1882</div></a><a href="https://stackoverflow.com/questions/9371238/why-is-reading-lines-from-stdin-much-slower-in-c-than-python?rq=1" class="question-hyperlink">Why is reading lines from stdin much slower in C++ than Python?</a></div><div class="spacer js-gps-track"><a href="https://stackoverflow.com/q/10168686?rq=1" title="Vote score (upvotes - downvotes)"><div class="answer-votes answered-accepted extra-large">1680</div></a><a href="https://stackoverflow.com/questions/10168686/image-processing-algorithm-improvement-for-coca-cola-can-recognition?rq=1" class="question-hyperlink">Image Processing: Algorithm Improvement for 'Coca-Cola Can' Recognition</a></div><div class="spacer js-gps-track"><a href="https://stackoverflow.com/q/11277432?rq=1" title="Vote score (upvotes - downvotes)"><div class="answer-votes answered-accepted extra-large">1883</div></a><a href="https://stackoverflow.com/questions/11277432/how-to-remove-a-key-from-a-python-dictionary?rq=1" class="question-hyperlink">How to remove a key from a Python dictionary?</a></div><div class="spacer js-gps-track"><a href="https://stackoverflow.com/q/15589517?rq=1" title="Vote score (upvotes - downvotes)"><div class="answer-votes answered-accepted large">243</div></a><a href="https://stackoverflow.com/questions/15589517/how-to-crop-an-image-in-opencv-using-python?rq=1" class="question-hyperlink">How to crop an image in OpenCV using Python</a></div><div class="spacer js-gps-track"><a href="https://stackoverflow.com/q/15969028?rq=1" title="Vote score (upvotes - downvotes)"><div class="answer-votes answered-accepted default">7</div></a><a href="https://stackoverflow.com/questions/15969028/crop-image-by-polygon-area?rq=1" class="question-hyperlink">Crop image by polygon area</a></div><div class="spacer js-gps-track"><a href="https://stackoverflow.com/q/24200556?rq=1" title="Vote score (upvotes - downvotes)"><div class="answer-votes default">2</div></a><a href="https://stackoverflow.com/questions/24200556/matlab-crop-a-polygon-from-an-image?rq=1" class="question-hyperlink">Matlab crop a polygon from an image</a></div><div class="spacer js-gps-track"><a href="https://stackoverflow.com/q/37725845?rq=1" title="Vote score (upvotes - downvotes)"><div class="answer-votes default">1</div></a><a href="https://stackoverflow.com/questions/37725845/opencv-crop-around-hough-circle-point-python?rq=1" class="question-hyperlink">OpenCV crop around Hough Circle point Python</a></div>
                        </div>
                    </div>

                <div id="hot-network-questions" class="module tex2jax_ignore">
    <h4>
        <a href="https://stackexchange.com/questions?tab=hot" class="js-gps-track s-link s-link__inherit" data-gps-track="posts_hot_network.click({ item_type:1, location:11 })">
            Hot Network Questions
        </a>
    </h4>
    <ul>
            <li>
                <div class="favicon favicon-english" title="English Language &amp; Usage Stack Exchange"></div><a href="https://english.stackexchange.com/questions/545632/what-is-the-first-mention-use-of-the-word-america-in-print-in-an-english-writt" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:97 }); posts_hot_network.click({ item_type:2, location:11 })">
                    What is the first mention/use of the word "America" in Print in an English written/translated source
                </a>

            </li>
            <li>
                <div class="favicon favicon-opensource" title="Open Source Stack Exchange"></div><a href="https://opensource.stackexchange.com/questions/10376/forbid-distribution-of-the-app-licensed-with-gpl-v3-in-certain-countries" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:619 }); posts_hot_network.click({ item_type:2, location:11 })">
                    Forbid distribution of the app licensed with GPL v3 in certain countries
                </a>

            </li>
            <li>
                <div class="favicon favicon-matheducators" title="Mathematics Educators Stack Exchange"></div><a href="https://matheducators.stackexchange.com/questions/18766/future-educators-writing-nonsense-questions" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:548 }); posts_hot_network.click({ item_type:2, location:11 })">
                    Future educators writing nonsense questions
                </a>

            </li>
            <li>
                <div class="favicon favicon-mathoverflow" title="MathOverflow"></div><a href="https://mathoverflow.net/questions/370762/complex-projective-manifolds-are-homeomorphic-if-homotopy-equivalent" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:504 }); posts_hot_network.click({ item_type:2, location:11 })">
                    Complex projective manifolds are homeomorphic if homotopy equivalent
                </a>

            </li>
            <li>
                <div class="favicon favicon-rpg" title="Role-playing Games Stack Exchange"></div><a href="https://rpg.stackexchange.com/questions/174965/the-bbeg-wants-to-delay-the-party-in-the-final-battle-monologue" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:122 }); posts_hot_network.click({ item_type:2, location:11 })">
                    The BBEG wants to delay the party in the final battle... (monologue?)
                </a>

            </li>
            <li class="js-hidden" style="">
                <div class="favicon favicon-interpersonal" title="Interpersonal Skills Stack Exchange"></div><a href="https://interpersonal.stackexchange.com/questions/26102/why-is-it-socially-not-acceptable-to-point-at-someone-with-your-finger" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:680 }); posts_hot_network.click({ item_type:2, location:11 })">
                    Why is it socially not acceptable to point at someone with your finger?
                </a>

            </li>
            <li class="js-hidden" style="">
                <div class="favicon favicon-mathoverflow" title="MathOverflow"></div><a href="https://mathoverflow.net/questions/370788/decomposing-a-colimit-by-decomposing-the-indexing-diagram" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:504 }); posts_hot_network.click({ item_type:2, location:11 })">
                    Decomposing a (co)limit by decomposing the indexing diagram
                </a>

            </li>
            <li class="js-hidden" style="">
                <div class="favicon favicon-money" title="Personal Finance &amp; Money Stack Exchange"></div><a href="https://money.stackexchange.com/questions/130551/why-is-live-nations-stock-trading-so-high-in-the-middle-of-a-pandemic-that-has" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:93 }); posts_hot_network.click({ item_type:2, location:11 })">
                    Why is Live Nation's stock trading so high in the middle of a pandemic that has brought its industry (live entertainment) to a total halt?
                </a>

            </li>
            <li class="js-hidden" style="">
                <div class="favicon favicon-economics" title="Economics Stack Exchange"></div><a href="https://economics.stackexchange.com/questions/39508/if-someone-goes-for-a-haircut-does-it-increase-gdp" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:591 }); posts_hot_network.click({ item_type:2, location:11 })">
                    If someone goes for a haircut, does it increase GDP?
                </a>

            </li>
            <li class="js-hidden" style="">
                <div class="favicon favicon-softwareengineering" title="Software Engineering Stack Exchange"></div><a href="https://softwareengineering.stackexchange.com/questions/415441/whats-the-use-case-for-formatting-monetary-values-with-a-system-dependent-cur" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:131 }); posts_hot_network.click({ item_type:2, location:11 })">
                    What's the use case for formatting monetary values with a *system-dependent* currency symbol?
                </a>

            </li>
            <li class="js-hidden" style="">
                <div class="favicon favicon-law" title="Law Stack Exchange"></div><a href="https://law.stackexchange.com/questions/55946/can-the-law-limit-what-heath-care-providers-i-see-if-i-have-commercial-and-medic" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:617 }); posts_hot_network.click({ item_type:2, location:11 })">
                    Can the law limit what heath care providers I see if I have commercial and medicaid?
                </a>

            </li>
            <li class="js-hidden" style="">
                <div class="favicon favicon-workplace" title="The Workplace Stack Exchange"></div><a href="https://workplace.stackexchange.com/questions/163559/what-to-do-when-you-discover-that-the-company-youre-about-to-have-a-job-intervi" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:423 }); posts_hot_network.click({ item_type:2, location:11 })">
                    What to do when you discover that the company you're about to have a job interview with recruited ex-colleagues that I can't stand?
                </a>

            </li>
            <li class="js-hidden" style="">
                <div class="favicon favicon-retrocomputing" title="Retrocomputing Stack Exchange"></div><a href="https://retrocomputing.stackexchange.com/questions/16046/what-was-the-first-file-system" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:648 }); posts_hot_network.click({ item_type:2, location:11 })">
                    What was the first file system?
                </a>

            </li>
            <li class="js-hidden" style="">
                <div class="favicon favicon-blender" title="Blender Stack Exchange"></div><a href="https://blender.stackexchange.com/questions/193249/how-would-i-make-an-indented-swirl-around-this-sphere" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:502 }); posts_hot_network.click({ item_type:2, location:11 })">
                    How would I make an indented swirl around this sphere
                </a>

            </li>
            <li class="js-hidden" style="">
                <div class="favicon favicon-chess" title="Chess Stack Exchange"></div><a href="https://chess.stackexchange.com/questions/32103/4-2-vs-3-3-only-pawn-endgames-arising-from-sicilian-anti-sicilian" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:435 }); posts_hot_network.click({ item_type:2, location:11 })">
                    4-2 vs 3-3 (only pawn) endgames arising from Sicilian/Anti Sicilian
                </a>

            </li>
            <li class="js-hidden" style="">
                <div class="favicon favicon-codegolf" title="Code Golf Stack Exchange"></div><a href="https://codegolf.stackexchange.com/questions/210437/prime-power-switch" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:200 }); posts_hot_network.click({ item_type:2, location:11 })">
                    Prime Power Switch
                </a>

            </li>
            <li class="js-hidden" style="">
                <div class="favicon favicon-politics" title="Politics Stack Exchange"></div><a href="https://politics.stackexchange.com/questions/56853/do-people-in-countries-besides-the-us-react-negatively-to-militarized-police" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:475 }); posts_hot_network.click({ item_type:2, location:11 })">
                    Do people in countries besides the US react negatively to "militarized police"?
                </a>

            </li>
            <li class="js-hidden" style="">
                <div class="favicon favicon-stats" title="Cross Validated"></div><a href="https://stats.stackexchange.com/questions/485784/which-distribution-has-its-maximum-uniformly-distributed" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:65 }); posts_hot_network.click({ item_type:2, location:11 })">
                    Which distribution has its maximum uniformly distributed?
                </a>

            </li>
            <li class="js-hidden" style="">
                <div class="favicon favicon-money" title="Personal Finance &amp; Money Stack Exchange"></div><a href="https://money.stackexchange.com/questions/130531/sugar-daddy-prepaid-card-scam" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:93 }); posts_hot_network.click({ item_type:2, location:11 })">
                    Sugar daddy prepaid card scam
                </a>

            </li>
            <li class="js-hidden" style="">
                <div class="favicon favicon-buddhism" title="Buddhism Stack Exchange"></div><a href="https://buddhism.stackexchange.com/questions/41389/am-i-following-buddhism-as-a-sort-of-escapism" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:565 }); posts_hot_network.click({ item_type:2, location:11 })">
                    Am I following Buddhism as a sort of Escapism?
                </a>

            </li>
            <li class="js-hidden" style="">
                <div class="favicon favicon-space" title="Space Exploration Stack Exchange"></div><a href="https://space.stackexchange.com/questions/46304/where-to-look-for-next-rocket-launches" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:508 }); posts_hot_network.click({ item_type:2, location:11 })">
                    Where to look for next rocket launches?
                </a>

            </li>
            <li class="js-hidden" style="">
                <div class="favicon favicon-space" title="Space Exploration Stack Exchange"></div><a href="https://space.stackexchange.com/questions/46333/did-sputnik-1-tell-us-more-than-beep-what-science-was-improved-by-information" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:508 }); posts_hot_network.click({ item_type:2, location:11 })">
                    Did Sputnik 1 tell us more than "beep"? What science was improved by information gained from its orbiting the Earth?
                </a>

            </li>
            <li class="js-hidden" style="">
                <div class="favicon favicon-bicycles" title="Bicycles Stack Exchange"></div><a href="https://bicycles.stackexchange.com/questions/71841/shimano-acera-hits-spokes-which-screw-to-turn" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:126 }); posts_hot_network.click({ item_type:2, location:11 })">
                    Shimano Acera hits spokes. Which screw to turn?
                </a>

            </li>
            <li class="js-hidden" style="">
                <div class="favicon favicon-workplace" title="The Workplace Stack Exchange"></div><a href="https://workplace.stackexchange.com/questions/163501/official-warning-by-a-manager-for-how-i-spend-my-vacations-escalate-or-ignore" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:423 }); posts_hot_network.click({ item_type:2, location:11 })">
                    Official warning by a manager for how I spend my vacations: escalate or ignore?
                </a>

            </li>
    </ul>

        
</div>

                            <div id="feed-link" class="js-feed-link">
        <a href="https://stackoverflow.com/feeds/question/48301186" title="Feed of this question and its answers">
            <svg aria-hidden="true" class="fc-orange-400 svg-icon iconRss" width="18" height="18" viewBox="0 0 18 18"><path d="M1 3c0-1.1.9-2 2-2h12a2 2 0 012 2v12a2 2 0 01-2 2H3a2 2 0 01-2-2V3zm14.5 12C15.5 8.1 9.9 2.5 3 2.5V5a10 10 0 0110 10h2.5zm-5 0A7.5 7.5 0 003 7.5V10a5 5 0 015 5h2.5zm-5 0A2.5 2.5 0 003 12.5V15h2.5z"></path></svg>
            Question feed
        </a>
    </div>
    <aside class="s-modal js-feed-link-modal" tabindex="-1" role="dialog" aria-labelledby="feed-modal-title" aria-describedby="feed-modal-description" aria-hidden="true">
        <div class="s-modal--dialog js-modal-dialog wmx4" role="document" data-controller="se-draggable">
            <h1 class="s-modal--header fw-bold js-first-tabbable c-move" id="feed-modal-title" data-target="se-draggable.handle" tabindex="0">
                Subscribe to RSS
            </h1>
            <div class="grid gs4 gsy fd-column">
                <div class="grid--cell">
                    <label class="d-block s-label c-default" for="feed-url">
                        Question feed
                        <p class="s-description mt2" id="feed-modal-description">To subscribe to this RSS feed, copy and paste this URL into your RSS reader.</p>
                    </label>
                </div>
                <div class="grid ps-relative">
                    <input class="s-input" type="text" name="feed-url" id="feed-url" readonly="readonly" value="https://stackoverflow.com/feeds/question/48301186">
                    <svg aria-hidden="true" class="s-input-icon fc-orange-400 svg-icon iconRss" width="18" height="18" viewBox="0 0 18 18"><path d="M1 3c0-1.1.9-2 2-2h12a2 2 0 012 2v12a2 2 0 01-2 2H3a2 2 0 01-2-2V3zm14.5 12C15.5 8.1 9.9 2.5 3 2.5V5a10 10 0 0110 10h2.5zm-5 0A7.5 7.5 0 003 7.5V10a5 5 0 015 5h2.5zm-5 0A2.5 2.5 0 003 12.5V15h2.5z"></path></svg>
                </div>
            </div>
            <a class="s-modal--close s-btn s-btn__muted js-modal-close js-last-tabbable" href="https://stackoverflow.com/questions/48301186/cropping-concave-polygon-from-image-using-opencv-python#" aria-label="Close">
                <svg aria-hidden="true" class="svg-icon iconClearSm" width="14" height="14" viewBox="0 0 14 14"><path d="M12 3.41L10.59 2 7 5.59 3.41 2 2 3.41 5.59 7 2 10.59 3.41 12 7 8.41 10.59 12 12 10.59 8.41 7 12 3.41z"></path></svg>
            </a>
        </div>
    </aside>

            </div>
    </div>
<script>StackExchange.ready(function(){$.get('/posts/48301186/ivc/0d93');});</script>
<noscript><div><img src="/posts/48301186/ivc/0d93" class="dno" alt="" width="0" height="0"></div></noscript><div style="display:none" id="js-codeblock-lang">lang-py</div></div>


        </div>
    </div>
        
<script>;try{(function(a){function b(a){return'string'==typeof a?document.getElementById(a):a}function c(a){return a=b(a),!!a&&'none'===getComputedStyle(a).display}function d(a){return!c(a)}function e(a){return!!a}function f(a){return /^\s*$/.test(b(a).innerHTML)}function g(a){var b=a.style;b.height=b.maxHeight=b.minHeight='auto',b.display='none'}function h(a){var b=a.style;b.height=b.maxHeight=b.minHeight='auto',b.display='none',[].forEach.call(a.children,h)}function i(a){var b=a.style;b.height=b.maxHeight=b.minHeight='auto',b.removeProperty('display')}function j(a,b){var c;return function(){return a&&(c=a.call(b||this,arguments),a=null),c}}function k(a){var b=document.createElement('script');b.src=a,document.body.appendChild(b)}function l(a){return m([],a)}function m(a,b){return a.push=function(a){return b(),delete this.push,this.push(a)},a}function n(){try{return!new Function('return async()=>{};')}catch(a){return!0}}function o(){return'undefined'!=typeof googletag&&!!googletag.apiReady}function p(){o()||(googletag={cmd:l(B)})}function q(){var a=document.createElement('div');a.className='adsbox',a.id='clc-abd',a.style.position='absolute',a.style.pointerEvents='none',a.innerHTML='&nbsp;',document.body.appendChild(a)}function r(){return Object.keys(F.ids)}function s(a){var b=F.ids[a],c=F.slots[b];'function'==typeof c&&(c=c(a));return{path:'/'+C+'/'+E+'/'+b+'/'+D,sizes:c,zone:b}}function t(a){try{Array.isArray(clc.dfp.slotsRenderedEvents)||(clc.dfp.slotsRenderedEvents=[]),clc.dfp.slotsRenderedEvents.push(a);var b=a.slot.getSlotElementId(),c=[];b||c.push('id=0');var d=document.getElementById(b);if(!b||d?d.hasAttribute('data-clc-stalled')&&c.push('st=1'):c.push('el=0'),0!==c.length)return void G(c.join('&'));var e=s(b),f=e.zone;if(clc.collapse&&clc.collapse[f]&&a.isEmpty)return h(d),void d.setAttribute('data-clc-ready','true');if(-1!==y.dh.indexOf(a.lineItemId))h(d);else if(a.lineItemId){d.setAttribute('data-clc-prefilled','true');var j=d.parentElement;if(j.classList.contains('js-zone-container')){g(j);var k=j.querySelectorAll('.js-report-ad-button-container'),l=k[0];switch(l.style.height='24px',b){case'dfp-tlb':case'dfp-tag':{j.classList.add('mb8');break}case'dfp-mlb':case'dfp-smlb':case'dfp-bmlb':{j.classList.add('my8');break}case'dfp-isb':{j.classList.add('mt24');break}case'dfp-m-aq':{j.classList.add('my12'),j.classList.add('mx-auto');break}default:}i(j),i(d)}else i(d);if('dfp-msb'==b){var m=document.getElementById('hireme');h(m)}}d.setAttribute('data-clc-ready','true')}catch(a){var n=document.querySelector('#dfp-tsb, #dfp-isb, #clc-tsb');n&&n.setAttribute('data-clc-ready','true'),G('e=1')}}function u(a,b){'dfp-isb'===a&&b.setTargeting('Sidebar',['Inline']),'dfp-tsb'===a&&b.setTargeting('Sidebar',['Right']);var c=s(a),d=c.path,e=c.sizes,f=c.zone,g=googletag.defineSlot(d,e,a);g.addService(b),!1}function v(b){var c=a.dfp&&a.dfp.targeting||{};'SystemDefault'===c.ProductVariant&&(window.matchMedia&&window.matchMedia('(prefers-color-scheme: dark)').matches?c.ProductVariant='Dark':c.ProductVariant='Light'),Object.keys(c).forEach(function(a){b.setTargeting(a,c[a])})}function w(a){var g=a.map(b).filter(e);return{eligible:g.filter(f).filter(d),ineligible:g.filter(c)}}function x(b){void 0===b&&(b=r());var c=['dfp-mlb','dfp-smlb'];if(!o())return p(),void googletag.cmd.push(function(){return x(b)});var d=w(b),e=d.eligible,f=d.ineligible;if(e.forEach(function(a){g(a)}),f.forEach(h),0!==e.length){y.abd&&q(),googletag.destroySlots();var i=googletag.pubads();y.sf&&(i.setForceSafeFrame(!0),i.setSafeFrameConfig({allowOverlayExpansion:!0,allowPushExpansion:!0,sandbox:!0})),y.ll||i.enableSingleRequest(),a.sreEvent||(i.addEventListener('slotRenderEnded',t),a.sreEvent=!0),v(i);var j=e.filter(function(a){return!y.ll||0>c.indexOf(a.id)}),k=e.filter(function(a){return!!y.ll&&0<=c.indexOf(a.id)});j.forEach(function(a){u(a.id,i),a.setAttribute('data-dfp-zone','true')}),googletag.enableServices(),j.forEach(function(a){googletag.display(a.id)}),y.ll&&(i.enableLazyLoad({fetchMarginPercent:0,renderMarginPercent:0}),k.forEach(function(a){u(a.id,i),a.setAttribute('data-clc-prefilled','true')}),k.forEach(function(a){googletag.display(a.id)}))}}var y=function(a){for(var b=[],c=1;c<arguments.length;c++)b[c-1]=arguments[c];for(var d,e=0,f=b;e<f.length;e++)for(var g in d=f[e],d)a[g]=d[g];return a}({"lib":"https://cdn.sstatic.net/clc/clc.min.js?v=d7c7e62bd2f5","style":"https://cdn.sstatic.net/clc/styles/clc.min.css?v=83419f27e8fa","u":"https://clc.stackoverflow.com/markup.js","wa":true,"kt":2000,"tto":true,"h":"clc.stackoverflow.com","allowed":"^(((talent\\.)?stackoverflow)|(blog\\.codinghorror)|(serverfault|askubuntu)|([^\\.]+\\.stackexchange))\\.com$","wv":true,"al":false,"dh":[5171832659],"abd":true},a.options||{}),z=j(function(){var a=y.lib;n()&&(a=a.replace(/(\.min)?\.js(\?v=[0-9a-fA-F]+)?$/,'.ie$1.js$2')),k(a)}),A=a.cmd||[];Array.isArray(A)&&(0<A.length?z():m(A,z));var B=j(function(){k('https://www.googletagservices.com/tag/js/gpt.js')}),C='248424177',D=/^\/tags\//.test(location.pathname)||/^\/questions\/tagged\//.test(location.pathname)?'tag-pages':/^\/$/.test(location.pathname)||/^\/home/.test(location.pathname)?'home-page':'question-pages',E=location.hostname;var F={slots:{lb:[[728,90]],mlb:[[728,90]],smlb:[[728,90]],bmlb:[[728,90]],sb:function(a){return'dfp-tsb'===a?[[300,250],[300,600]]:[[300,250]]},"tag-sponsorship":[[730,135]],"mobile-below-question":[[320,50],[300,250]],msb:[[300,250],[300,600]]},ids:{"dfp-tlb":'lb',"dfp-mlb":'mlb',"dfp-smlb":'smlb',"dfp-bmlb":'bmlb',"dfp-tsb":'sb',"dfp-isb":'sb',"dfp-tag":'tag-sponsorship',"dfp-msb":'msb',"dfp-m-aq":'mobile-below-question',"clc-tlb":'lb',"clc-mlb":'mlb',"clc-tsb":'sb'}},G=function(a){new Image().src='https://'+y.h+'/stalled.gif?'+a};(function(){var b=y.al;b&&A.push(function(){return a.load()})})(),p(),a.dfp={load:x},a.options=y,a.cmd=A})(this.clc=this.clc||{})}catch(a){window.console.error(a)}</script>    <script>
        var clc = clc || {};
        clc.collapse = { sb: !0, 'tag-sponsorship': !0, lb: !0, mlb: !0, smlb: !0, bmlb: !0, 'mobile-below-question': !0 };
        clc.options = clc.options || {};
        clc.options.sf = !0;
        clc.options.hb = !1;
        clc.options.ll = !0;
        clc.cmd = clc.cmd || [];
        clc.cmd.push(function () { window.clc_request='ApZljErEUNgIAAAAAIIE4QICAAAAAgAAAAAlAAAAfHB5dGhvbnxvcGVuY3Z8aW1hZ2UtcHJvY2Vzc2luZ3xjcm9wfACuIvGD7YEtNW5A'; clc.load(); });
        clc.dfp = clc.dfp || {};
        clc.dfp.targeting = {Registered:['false'],'so-tag':['python','opencv','image-processing','crop'],'tag-reportable':['python','opencv','image-processing','crop'],'tag-non-reportable':['python','opencv','image-processing','crop'],NumberOfAnswers:['2']};
        var googletag = googletag || {};
        googletag.cmd = googletag.cmd || [];
        googletag.cmd.push(function () { clc.dfp.load(); });

            StackExchange.ready(function () { googletag.cmd.push(function () { StackExchange.ads.init(googletag, '/ads/report-ad', 'Report this ad') }) });
    </script><script src="./none_files/clc.min.js.download"></script><script src="./none_files/gpt.js.download"></script>

            <footer id="footer" class="site-footer js-footer" role="contentinfo">
        <div class="site-footer--container">
                <div class="site-footer--logo">
                    
                    <a href="https://stackoverflow.com/"><svg aria-hidden="true" class="native svg-icon iconLogoGlyphMd" width="32" height="37" viewBox="0 0 32 37"><path d="M26 33v-9h4v13H0V24h4v9h22z" fill="#BCBBBB"></path><path d="M21.5 0l-2.7 2 9.9 13.3 2.7-2L21.5 0zM26 18.4L13.3 7.8l2.1-2.5 12.7 10.6-2.1 2.5zM9.1 15.2l15 7 1.4-3-15-7-1.4 3zm14 10.79l.68-2.95-16.1-3.35L7 23l16.1 2.99zM23 30H7v-3h16v3z" fill="#F48024"></path></svg></a>
                </div>
            <nav class="site-footer--nav">
                    <div class="site-footer--col site-footer--col__visible js-footer-col" data-name="default">
                        <h5 class="-title"><a href="https://stackoverflow.com/" class="js-gps-track" data-gps-track="footer.click({ location: 2, link: 15})">Stack Overflow</a></h5>
                        <ul class="-list js-primary-footer-links">
                            <li class="-item"><a href="https://stackoverflow.com/questions" class="js-gps-track -link" data-gps-track="footer.click({ location: 2, link: 16})">Questions</a></li>
                                <li class="-item"><a href="https://stackoverflow.com/jobs" class="js-gps-track -link" data-gps-track="footer.click({ location: 2, link: 17})">Jobs</a></li>
                                <li class="-item"><a href="https://stackoverflow.com/jobs/directory/developer-jobs" class="js-gps-track -link" data-gps-track="footer.click({ location: 2, link: 11})">Developer Jobs Directory</a></li>
                                     <li class="-item"><a href="https://stackoverflow.com/jobs/salary" class="js-gps-track -link" data-gps-track="footer.click({ location: 2, link: 28})">Salary Calculator</a></li>
                                <li class="-item"><a href="https://stackoverflow.com/help" class="js-gps-track -link" data-gps-track="footer.click({ location: 2, link: 3 })">Help</a></li>
                                <li class="-item"><a onclick="StackExchange.switchMobile(&quot;on&quot;)" class="js-gps-track -link" data-gps-track="footer.click({ location: 2, link: 12 })">Mobile</a></li>
                        <li class="-item"><a class="-link" role="button">Disable Responsiveness</a></li></ul>
                    </div>
                    <div class="site-footer--col site-footer--col__visible js-footer-col" data-name="default">
                        <h5 class="-title"><a href="https://stackoverflowbusiness.com/" class="js-gps-track" data-gps-track="footer.click({ location: 2, link: 19 })">Products</a></h5>
                        <ul class="-list">
                            <li class="-item"><a href="https://stackoverflow.com/teams" class="js-gps-track -link" data-ga="[&quot;teams traffic&quot;,&quot;footer - site nav&quot;,&quot;stackoverflow.com/teams&quot;,null,{&quot;dimension4&quot;:&quot;teams&quot;}]" data-gps-track="footer.click({ location: 2, link: 29 })">Teams</a></li>
                            <li class="-item"><a href="https://stackoverflow.com/talent" class="js-gps-track -link" data-gps-track="footer.click({ location: 2, link: 20 })">Talent</a></li>
                            <li class="-item"><a href="https://stackoverflow.com/advertising" class="js-gps-track -link" data-gps-track="footer.click({ location: 2, link: 21 })">Advertising</a></li>
                            <li class="-item"><a href="https://stackoverflow.com/enterprise" class="js-gps-track -link" data-gps-track="footer.click({ location: 2, link: 22 })">Enterprise</a></li>
                        </ul>
                    </div>
                <div class="site-footer--col site-footer--col__visible js-footer-col" data-name="default">
                    <h5 class="-title"><a class="js-gps-track" data-gps-track="footer.click({ location: 2, link: 1 })" href="https://stackoverflow.com/company">Company</a></h5>
                    <ul class="-list">
                            <li class="-item"><a class="js-gps-track -link" data-gps-track="footer.click({ location: 2, link: 1 })" href="https://stackoverflow.com/company">About</a></li>
                        <li class="-item"><a class="js-gps-track -link" data-gps-track="footer.click({ location: 2, link: 27 })" href="https://stackoverflow.com/company/press">Press</a></li>
                            <li class="-item"><a class="js-gps-track -link" data-gps-track="footer.click({ location: 2, link: 9 })" href="https://stackoverflow.com/company/work-here">Work Here</a></li>
                        <li class="-item"><a class="js-gps-track -link" data-gps-track="footer.click({ location: 2, link: 7 })" href="https://stackoverflow.com/legal">Legal</a></li>
                        <li class="-item"><a class="js-gps-track -link" data-gps-track="footer.click({ location: 2, link: 8 })" href="https://stackoverflow.com/legal/privacy-policy">Privacy Policy</a></li>
                            <li class="-item"><a class="js-gps-track -link" data-gps-track="footer.click({ location: 2, link: 13 })" href="https://stackoverflow.com/company/contact">Contact Us</a></li>
                    </ul>
                </div>
                <div class="site-footer--col site-footer--categories-nav site-footer--col__visible">
                    <a href="https://stackoverflow.com/questions/48301186/cropping-concave-polygon-from-image-using-opencv-python#" class="site-footer--back js-footer-back"><svg aria-hidden="true" class="svg-icon iconArrowLeftAlt" width="18" height="18" viewBox="0 0 18 18"><path d="M10.58 16L12 14.59 6.4 9 12 3.41 10.57 2l-7 7 7 7z"></path></svg></a>
                    <div>
                        <h5 class="-title"><a href="https://stackexchange.com/" data-gps-track="footer.click({ location: 2, link: 30 })">Stack Exchange<br> Network</a></h5>
                        <ul class="-list">
                            <li class="-item"><a href="https://stackoverflow.com/questions/48301186/cropping-concave-polygon-from-image-using-opencv-python#" class="-link _expandable js-footer-category-trigger js-gps-track" data-gps-track="footer.click({ location: 2, link: 24 })" data-target="Technology">Technology</a></li>
                            <li class="-item"><a href="https://stackoverflow.com/questions/48301186/cropping-concave-polygon-from-image-using-opencv-python#" class="-link _expandable js-footer-category-trigger js-gps-track" data-gps-track="footer.click({ location: 2, link: 24 })" data-target="Life / Arts">Life / Arts</a></li>
                            <li class="-item"><a href="https://stackoverflow.com/questions/48301186/cropping-concave-polygon-from-image-using-opencv-python#" class="-link _expandable js-footer-category-trigger js-gps-track" data-gps-track="footer.click({ location: 2, link: 24 })" data-target="Culture / Recreation">Culture / Recreation</a></li>
                            <li class="-item"><a href="https://stackoverflow.com/questions/48301186/cropping-concave-polygon-from-image-using-opencv-python#" class="-link _expandable js-footer-category-trigger js-gps-track" data-gps-track="footer.click({ location: 2, link: 24 })" data-target="Science">Science</a></li>
                            <li class="-item"><a href="https://stackoverflow.com/questions/48301186/cropping-concave-polygon-from-image-using-opencv-python#" class="-link _expandable js-footer-category-trigger js-gps-track" data-gps-track="footer.click({ location: 2, link: 24 })" data-target="Other">Other</a></li>
                        </ul>
                    </div>
                </div>
                <div class="site-footer--categories">
                        <div class="site-footer--col site-footer--category js-footer-col" data-name="Technology">
        <ul class="-list">
                <li class="-item"><a href="https://stackoverflow.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="professional and enthusiast programmers">Stack Overflow</a></li>
                <li class="-item"><a href="https://serverfault.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="system and network administrators">Server Fault</a></li>
                <li class="-item"><a href="https://superuser.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="computer enthusiasts and power users">Super User</a></li>
                <li class="-item"><a href="https://webapps.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="power users of web applications">Web Applications</a></li>
                <li class="-item"><a href="https://askubuntu.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="Ubuntu users and developers">Ask Ubuntu</a></li>
                <li class="-item"><a href="https://webmasters.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="pro webmasters">Webmasters</a></li>
                <li class="-item"><a href="https://gamedev.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="professional and independent game developers">Game Development</a></li>
                    </ul></div><div class="site-footer--col site-footer--category js-footer-col" data-name="Technology"><ul class="-list">
                <li class="-item"><a href="https://tex.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="users of TeX, LaTeX, ConTeXt, and related typesetting systems">TeX - LaTeX</a></li>
                <li class="-item"><a href="https://softwareengineering.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="professionals, academics, and students working within the systems development life cycle">Software Engineering</a></li>
                <li class="-item"><a href="https://unix.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="users of Linux, FreeBSD and other Un*x-like operating systems">Unix &amp; Linux</a></li>
                <li class="-item"><a href="https://apple.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="power users of Apple hardware and software">Ask Different (Apple)</a></li>
                <li class="-item"><a href="https://wordpress.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="WordPress developers and administrators">WordPress Development</a></li>
                <li class="-item"><a href="https://gis.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="cartographers, geographers and GIS professionals">Geographic Information Systems</a></li>
                <li class="-item"><a href="https://electronics.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="electronics and electrical engineering professionals, students, and enthusiasts">Electrical Engineering</a></li>
                    </ul></div><div class="site-footer--col site-footer--category js-footer-col" data-name="Technology"><ul class="-list">
                <li class="-item"><a href="https://android.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="enthusiasts and power users of the Android operating system">Android Enthusiasts</a></li>
                <li class="-item"><a href="https://security.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="information security professionals">Information Security</a></li>
                <li class="-item"><a href="https://dba.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="database professionals who wish to improve their database skills and learn from others in the community">Database Administrators</a></li>
                <li class="-item"><a href="https://drupal.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="Drupal developers and administrators">Drupal Answers</a></li>
                <li class="-item"><a href="https://sharepoint.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="SharePoint enthusiasts">SharePoint</a></li>
                <li class="-item"><a href="https://ux.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="user experience researchers and experts">User Experience</a></li>
                <li class="-item"><a href="https://mathematica.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="users of Wolfram Mathematica">Mathematica</a></li>
                    </ul></div><div class="site-footer--col site-footer--category js-footer-col" data-name="Technology"><ul class="-list">
                <li class="-item"><a href="https://salesforce.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="Salesforce administrators, implementation experts, developers and anybody in-between">Salesforce</a></li>
                <li class="-item"><a href="https://expressionengine.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="administrators, end users, developers and designers for ExpressionEngine® CMS">ExpressionEngine® Answers</a></li>
                <li class="-item"><a href="https://pt.stackoverflow.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="programadores profissionais e entusiastas">Stack Overflow em Português</a></li>
                <li class="-item"><a href="https://blender.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="people who use Blender to create 3D graphics, animations, or games">Blender</a></li>
                <li class="-item"><a href="https://networkengineering.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="network engineers">Network Engineering</a></li>
                <li class="-item"><a href="https://crypto.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="software developers, mathematicians and others interested in cryptography">Cryptography</a></li>
                <li class="-item"><a href="https://codereview.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="peer programmer code reviews">Code Review</a></li>
                    </ul></div><div class="site-footer--col site-footer--category js-footer-col" data-name="Technology"><ul class="-list">
                <li class="-item"><a href="https://magento.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="users of the Magento e-Commerce platform">Magento</a></li>
                <li class="-item"><a href="https://softwarerecs.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="people seeking specific software recommendations">Software Recommendations</a></li>
                <li class="-item"><a href="https://dsp.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="practitioners of the art and science of signal, image and video processing">Signal Processing</a></li>
                <li class="-item"><a href="https://emacs.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="those using, extending or developing Emacs">Emacs</a></li>
                <li class="-item"><a href="https://raspberrypi.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="users and developers of hardware and software for Raspberry Pi">Raspberry Pi</a></li>
                <li class="-item"><a href="https://ru.stackoverflow.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="программистов">Stack Overflow на русском</a></li>
                <li class="-item"><a href="https://codegolf.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="programming puzzle enthusiasts and code golfers">Code Golf</a></li>
                    </ul></div><div class="site-footer--col site-footer--category js-footer-col" data-name="Technology"><ul class="-list">
                <li class="-item"><a href="https://es.stackoverflow.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="programadores y profesionales de la informática">Stack Overflow en español</a></li>
                <li class="-item"><a href="https://ethereum.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="users of Ethereum, the decentralized application platform and smart contract enabled blockchain">Ethereum</a></li>
                <li class="-item"><a href="https://datascience.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="Data science professionals, Machine Learning specialists, and those interested in learning more about the field">Data Science</a></li>
                <li class="-item"><a href="https://arduino.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="developers of open-source hardware and software that is compatible with Arduino">Arduino</a></li>
                <li class="-item"><a href="https://bitcoin.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="Bitcoin crypto-currency enthusiasts">Bitcoin</a></li>
                <li class="-item"><a href="https://sqa.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="software quality control experts, automation engineers, and software testers">Software Quality Assurance &amp; Testing</a></li>
                <li class="-item"><a href="https://sound.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="sound engineers, producers, editors, and enthusiasts">Sound Design</a></li>
                    </ul></div><div class="site-footer--col site-footer--category js-footer-col" data-name="Technology"><ul class="-list">
                <li class="-item"><a href="https://windowsphone.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="enthusiasts and power users of Windows Phone OS">Windows Phone</a></li>
                <li class="-item">
                    <a href="https://stackexchange.com/sites#technology" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 26 })">
                        <strong>
                            more (28)
                        </strong>
                    </a>
                </li>
        </ul>
    </div>
    <div class="site-footer--col site-footer--category js-footer-col" data-name="Life / Arts">
        <ul class="-list">
                <li class="-item"><a href="https://photo.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="professional, enthusiast and amateur photographers">Photography</a></li>
                <li class="-item"><a href="https://scifi.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="science fiction and fantasy enthusiasts">Science Fiction &amp; Fantasy</a></li>
                <li class="-item"><a href="https://graphicdesign.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="Graphic Design professionals, students, and enthusiasts">Graphic Design</a></li>
                <li class="-item"><a href="https://movies.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="movie and TV enthusiasts">Movies &amp; TV</a></li>
                <li class="-item"><a href="https://music.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="musicians, students, and enthusiasts">Music: Practice &amp; Theory</a></li>
                <li class="-item"><a href="https://worldbuilding.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="writers/artists using science, geography and culture to construct imaginary worlds and settings">Worldbuilding</a></li>
                <li class="-item"><a href="https://video.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="engineers, producers, editors, and enthusiasts spanning the fields of video, and media creation">Video Production</a></li>
                    </ul></div><div class="site-footer--col site-footer--category js-footer-col" data-name="Life / Arts"><ul class="-list">
                <li class="-item"><a href="https://cooking.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="professional and amateur chefs">Seasoned Advice (cooking)</a></li>
                <li class="-item"><a href="https://diy.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="contractors and serious DIYers">Home Improvement</a></li>
                <li class="-item"><a href="https://money.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="people who want to be financially literate">Personal Finance &amp; Money</a></li>
                <li class="-item"><a href="https://academia.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="academics and those enrolled in higher education">Academia</a></li>
                <li class="-item"><a href="https://law.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="legal professionals, students, and others with experience or interest in law">Law</a></li>
                <li class="-item"><a href="https://fitness.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="physical fitness professionals, athletes, trainers, and those providing health-related needs">Physical Fitness</a></li>
                <li class="-item"><a href="https://gardening.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="gardeners and landscapers">Gardening &amp; Landscaping</a></li>
                    </ul></div><div class="site-footer--col site-footer--category js-footer-col" data-name="Life / Arts"><ul class="-list">
                <li class="-item"><a href="https://parenting.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="parents, grandparents, nannies and others with a parenting role">Parenting</a></li>
                <li class="-item">
                    <a href="https://stackexchange.com/sites#lifearts" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 26 })">
                        <strong>
                            more (10)
                        </strong>
                    </a>
                </li>
        </ul>
    </div>
    <div class="site-footer--col site-footer--category js-footer-col" data-name="Culture / Recreation">
        <ul class="-list">
                <li class="-item"><a href="https://english.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="linguists, etymologists, and serious English language enthusiasts">English Language &amp; Usage</a></li>
                <li class="-item"><a href="https://skeptics.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="scientific skepticism">Skeptics</a></li>
                <li class="-item"><a href="https://judaism.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="those who base their lives on Jewish law and tradition and anyone interested in learning more">Mi Yodeya (Judaism)</a></li>
                <li class="-item"><a href="https://travel.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="road warriors and seasoned travelers">Travel</a></li>
                <li class="-item"><a href="https://christianity.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="committed Christians, experts in Christianity and those interested in learning more">Christianity</a></li>
                <li class="-item"><a href="https://ell.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="speakers of other languages learning English">English Language Learners</a></li>
                <li class="-item"><a href="https://japanese.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="students, teachers, and linguists wanting to discuss the finer points of the Japanese language">Japanese Language</a></li>
                    </ul></div><div class="site-footer--col site-footer--category js-footer-col" data-name="Culture / Recreation"><ul class="-list">
                <li class="-item"><a href="https://chinese.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="students, teachers, and linguists wanting to discuss the finer points of the Chinese language">Chinese Language</a></li>
                <li class="-item"><a href="https://french.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="students, teachers, and linguists wanting to discuss the finer points of the French language">French Language</a></li>
                <li class="-item"><a href="https://german.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="speakers of German wanting to discuss the finer points of the language and translation">German Language</a></li>
                <li class="-item"><a href="https://hermeneutics.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="professors, theologians, and those interested in exegetical analysis of biblical texts">Biblical Hermeneutics</a></li>
                <li class="-item"><a href="https://history.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="historians and history buffs">History</a></li>
                <li class="-item"><a href="https://spanish.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="linguists, teachers, students and Spanish language enthusiasts in general wanting to discuss the finer points of the language">Spanish Language</a></li>
                <li class="-item"><a href="https://islam.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="Muslims, experts in Islam, and those interested in learning more about Islam">Islam</a></li>
                    </ul></div><div class="site-footer--col site-footer--category js-footer-col" data-name="Culture / Recreation"><ul class="-list">
                <li class="-item"><a href="https://rus.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="лингвистов и энтузиастов русского языка">Русский язык</a></li>
                <li class="-item"><a href="https://russian.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="students, teachers, and linguists wanting to discuss the finer points of the Russian language">Russian Language</a></li>
                <li class="-item"><a href="https://gaming.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="passionate videogamers on all platforms">Arqade (gaming)</a></li>
                <li class="-item"><a href="https://bicycles.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="people who build and repair bicycles, people who train cycling, or commute on bicycles">Bicycles</a></li>
                <li class="-item"><a href="https://rpg.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="gamemasters and players of tabletop, paper-and-pencil role-playing games">Role-playing Games</a></li>
                <li class="-item"><a href="https://anime.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="anime and manga fans">Anime &amp; Manga</a></li>
                <li class="-item"><a href="https://puzzling.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="those who create, solve, and study puzzles">Puzzling</a></li>
                    </ul></div><div class="site-footer--col site-footer--category js-footer-col" data-name="Culture / Recreation"><ul class="-list">
                <li class="-item"><a href="https://mechanics.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="mechanics and DIY enthusiast owners of cars, trucks, and motorcycles">Motor Vehicle Maintenance &amp; Repair</a></li>
                <li class="-item"><a href="https://boardgames.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="people who like playing board games, designing board games or modifying the rules of existing board games">Board &amp; Card Games</a></li>
                <li class="-item"><a href="https://bricks.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="LEGO® and building block enthusiasts">Bricks</a></li>
                <li class="-item"><a href="https://homebrew.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="dedicated home brewers and serious enthusiasts">Homebrewing</a></li>
                <li class="-item"><a href="https://martialarts.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="students and teachers of all martial arts">Martial Arts</a></li>
                <li class="-item"><a href="https://outdoors.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="people who love being outdoors enjoying nature and wilderness, and learning about the required skills and equipment">The Great Outdoors</a></li>
                <li class="-item"><a href="https://poker.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="serious players and enthusiasts of poker">Poker</a></li>
                    </ul></div><div class="site-footer--col site-footer--category js-footer-col" data-name="Culture / Recreation"><ul class="-list">
                <li class="-item"><a href="https://chess.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="serious players and enthusiasts of chess">Chess</a></li>
                <li class="-item"><a href="https://sports.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="participants in team and individual sport activities">Sports</a></li>
                <li class="-item">
                    <a href="https://stackexchange.com/sites#culturerecreation" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 26 })">
                        <strong>
                            more (16)
                        </strong>
                    </a>
                </li>
        </ul>
    </div>
    <div class="site-footer--col site-footer--category js-footer-col" data-name="Science">
        <ul class="-list">
                <li class="-item"><a href="https://mathoverflow.net/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="professional mathematicians">MathOverflow</a></li>
                <li class="-item"><a href="https://math.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="people studying math at any level and professionals in related fields">Mathematics</a></li>
                <li class="-item"><a href="https://stats.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="people interested in statistics, machine learning, data analysis, data mining, and data visualization">Cross Validated (stats)</a></li>
                <li class="-item"><a href="https://cstheory.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="theoretical computer scientists and researchers in related fields">Theoretical Computer Science</a></li>
                <li class="-item"><a href="https://physics.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="active researchers, academics and students of physics">Physics</a></li>
                <li class="-item"><a href="https://chemistry.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="scientists, academics, teachers, and students in the field of chemistry">Chemistry</a></li>
                <li class="-item"><a href="https://biology.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="biology researchers, academics, and students">Biology</a></li>
                    </ul></div><div class="site-footer--col site-footer--category js-footer-col" data-name="Science"><ul class="-list">
                <li class="-item"><a href="https://cs.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="students, researchers and practitioners of computer science">Computer Science</a></li>
                <li class="-item"><a href="https://philosophy.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="those interested in the study of the fundamental nature of knowledge, reality, and existence">Philosophy</a></li>
                <li class="-item"><a href="https://linguistics.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="professional linguists and others with an interest in linguistic research and theory">Linguistics</a></li>
                <li class="-item"><a href="https://psychology.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="practitioners, researchers, and students in cognitive science, psychology, neuroscience, and psychiatry">Psychology &amp; Neuroscience</a></li>
                <li class="-item"><a href="https://scicomp.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="scientists using computers to solve scientific problems">Computational Science</a></li>
                <li class="-item">
                    <a href="https://stackexchange.com/sites#science" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 26 })">
                        <strong>
                            more (10)
                        </strong>
                    </a>
                </li>
        </ul>
    </div>
    <div class="site-footer--col site-footer--category js-footer-col" data-name="Other">
        <ul class="-list">
                <li class="-item"><a href="https://meta.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="meta-discussion of the Stack Exchange family of Q&amp;A websites">Meta Stack Exchange</a></li>
                <li class="-item"><a href="https://stackapps.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="apps, scripts, and development with the Stack Exchange API">Stack Apps</a></li>
                <li class="-item"><a href="https://api.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="programmatic interaction with Stack Exchange sites">API</a></li>
                <li class="-item"><a href="https://data.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 25 })" title="querying Stack Exchange data using SQL">Data</a></li>
        </ul>
    </div>

                </div>
            </nav>
            <div class="site-footer--copyright fs-fine">
                <ul class="-list">
                    <li class="-item"><a class="js-gps-track -link" data-gps-track="footer.click({ location: 2, link:4 })" href="https://stackoverflow.blog/?blb=1">Blog</a></li>
                    <li class="-item"><a href="https://www.facebook.com/officialstackoverflow/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 31 })">Facebook</a></li>
                    <li class="-item"><a href="https://twitter.com/stackoverflow" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 32 })">Twitter</a></li>
                    <li class="-item"><a href="https://linkedin.com/company/stack-overflow" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 33 })">LinkedIn</a></li>
                    <li class="-item"><a href="https://www.instagram.com/thestackoverflow" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 36 })">Instagram</a></li>
                </ul>

                <p class="mt-auto mb24">
site design / logo © 2020 Stack Exchange Inc; user contributions licensed under <a href="https://stackoverflow.com/help/licensing">cc by-sa</a>.                    <span id="svnrev">rev&nbsp;2020.9.3.37555</span>
                </p>
            </div>
        </div>

    </footer>

            <script>StackExchange.ready(function () { StackExchange.responsiveness.addSwitcher(); })</script>
    <noscript>
        <div id="noscript-warning">Stack Overflow works best with JavaScript enabled
            <img src="https://pixel.quantserve.com/pixel/p-c1rF4kxgLUzNc.gif" alt="" class="dno">
        </div>
    </noscript>

            <script>
(function(i, s, o, g, r, a, m) {
                i['GoogleAnalyticsObject'] = r; i[r] = i[r] || function() { (i[r].q = i[r].q || []).push(arguments) }, i[r].l = 1 * new Date(); a = s.createElement(o),
                m = s.getElementsByTagName(o)[0]; a.async = 1; a.src = g; m.parentNode.insertBefore(a, m);
            })(window, document, 'script', 'https://www.google-analytics.com/analytics.js', 'ga');

            StackExchange.ready(function () {

                StackExchange.ga.init({
                    sendTitles: true,
                    tracker: window.ga,
                    trackingCodes: [
                        'UA-108242619-1'
                    ],
                        checkDimension: 'dimension42'
                });



                    StackExchange.ga.setDimension('dimension2', '|python|opencv|image-processing|crop|');

                    StackExchange.ga.setDimension('dimension3', 'Questions/Show');


                StackExchange.ga.trackPageView();
            });
            /**/

            var _qevents = _qevents || [],
            _comscore = _comscore || [];
            (function() {
                var s = document.getElementsByTagName('script')[0],
                    qc = document.createElement('script');
 qc.async = true;
                    qc.src = 'https://secure.quantserve.com/quant.js';
                    s.parentNode.insertBefore(qc, s);
                    _qevents.push({ qacct: "p-c1rF4kxgLUzNc" });/**/
 var sc = document.createElement('script');
                    sc.async = true;
                    sc.src = 'https://sb.scorecardresearch.com/beacon.js';
                    s.parentNode.insertBefore(sc, s);
                    _comscore.push({ c1: "2", c2: "17440561" });            })();
                </script>

    
    
    
<div class="adsbox" id="clc-abd" style="position: absolute; pointer-events: none;">&nbsp;</div><script src="./none_files/markup.js.download"></script><iframe id="google_osd_static_frame_183900047137" name="google_osd_static_frame" style="display: none; width: 0px; height: 0px;" src="./none_files/saved_resource.html"></iframe></body></html>