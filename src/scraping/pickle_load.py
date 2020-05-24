import pickle

#links = pickle.load( open( "nyc_links.pkl", "rb" ) )
#print(links)

# ls = ['https://www.goodtherapy.org/therapists/profile/laura-spinelli-20180804', 'https://www.goodtherapy.org/therapists/profile/victoria-morabito-20150724', 
# 'https://www.goodtherapy.org/therapists/profile/kenya-washington--20190421', 'https://www.goodtherapy.org/therapists/profile/marianne-esolen-20080413', 
# 'https://www.goodtherapy.org/therapists/profile/stephanie-colace-20190513', 'https://www.goodtherapy.org/therapists/profile/karen-kieser-20180408', 
# 'https://www.goodtherapy.org/therapists/profile/paula-gilbert-20160917', 'https://www.goodtherapy.org/therapists/profile/daniel-sapen-20100611', 
# 'https://www.goodtherapy.org/therapists/profile/kay-posillico-20161025', 'https://www.goodtherapy.org/therapists/profile/carol-pironi-20170417', 
# 'https://www.goodtherapy.org/therapists/profile/dominique-padmore-20200220', 'https://www.goodtherapy.org/therapists/profile/kalli-kontos-20100115', 
# 'https://www.goodtherapy.org/therapists/profile/kristin-li-20170130', 'https://www.goodtherapy.org/therapists/profile/christine-slobodin-20140718', 
# 'https://www.goodtherapy.org/therapists/profile/cynthia-luik-20160205', 'https://www.goodtherapy.org/therapists/profile/andrew-benevento', 
# 'https://www.goodtherapy.org/therapists/profile/dawn-cheetham-20110412', 'https://www.goodtherapy.org/therapists/profile/kerri-morris-20200518', 
# 'https://www.goodtherapy.org/therapists/profile/kyla-e-black-20130422', 'https://www.goodtherapy.org/therapists/profile/laura-brielmeier-20150131', 
# 'https://www.goodtherapy.org/therapists/profile/glenn-wolff-20120430', 'https://www.goodtherapy.org/therapists/profile/andrew-golden-20190424', 
# 'https://www.goodtherapy.org/therapists/profile/carissa-ali-20180819', 'https://www.goodtherapy.org/therapists/profile/gina-radicevella-20180929', 
# 'https://www.goodtherapy.org/therapists/profile/agnes-raczynski-20181216', 'https://www.goodtherapy.org/therapists/profile/Marc-Wax', 
# 'https://www.goodtherapy.org/therapists/profile/nancy-sidhu-20171005', 'https://www.goodtherapy.org/therapists/profile/frances-thuro-20090502', 
# 'https://www.goodtherapy.org/therapists/profile/stephanie-gaspari-20180610', 'https://www.goodtherapy.org/therapists/profile/jennifer-nielsen-20170710', 
# 'https://www.goodtherapy.org/therapists/profile/kerri-weiss-20200211', 'https://www.goodtherapy.org/therapists/profile/daphne-camille', 
# 'https://www.goodtherapy.org/therapists/profile/stacey-chernin-20130703', 'https://www.goodtherapy.org/therapists/profile/edward-regensburg-20100128', 
# 'https://www.goodtherapy.org/therapists/profile/tabitha-gonzalez-20171015', 'https://www.goodtherapy.org/therapists/profile/laura-vraney-20190221', 
# 'https://www.goodtherapy.org/therapists/profile/deirdre-a-cole-20091108', 'https://www.goodtherapy.org/therapists/profile/jessica-deluca-20190919', 
# 'https://www.goodtherapy.org/therapists/profile/isabel-frankel-rachlin-20130708', 'https://www.goodtherapy.org/therapists/profile/christine-lawlor-20101204', 
# 'https://www.goodtherapy.org/therapists/profile/ena-edouard-20191224', 'https://www.goodtherapy.org/therapists/profile/ashley-appleton-20190730', 
# 'https://www.goodtherapy.org/therapists/profile/marion-rollings-20120827', 'https://www.goodtherapy.org/therapists/profile/liz-ikle-20091117', 
# 'https://www.goodtherapy.org/therapists/profile/sherry-delia-20150217', 'https://www.goodtherapy.org/therapists/profile/r-ellen-runyon-20191228', 
# 'https://www.goodtherapy.org/therapists/profile/shan-reeves-20150919', 'https://www.goodtherapy.org/therapists/profile/nicholas-despoelberch--20180215', 
# 'https://www.goodtherapy.org/therapists/profile/aileen-blitz-20181230', 'https://www.goodtherapy.org/therapists/profile/cliff-koblin-20110425', 
# 'https://www.goodtherapy.org/therapists/profile/dorine-dangelo-20141107', 'https://www.goodtherapy.org/therapists/profile/laura-mercogliano-20181006', 
# 'https://www.goodtherapy.org/therapists/profile/asimena-charalambidisurban-20190218', 'https://www.goodtherapy.org/therapists/profile/letitia-brown-20170622', 
# 'https://www.goodtherapy.org/therapists/profile/Rikki%20Lyn-Hauss-McCarthy', 'https://www.goodtherapy.org/therapists/profile/peter-a-miller-20130324', 
# 'https://www.goodtherapy.org/therapists/profile/jane-martin-20141224', 'https://www.goodtherapy.org/therapists/profile/vincent-franco-20200407', 
# 'https://www.goodtherapy.org/therapists/profile/danielle-bissett-20180807', 'https://www.goodtherapy.org/therapists/profile/joseph-volpe-20090205', 
# 'https://www.goodtherapy.org/therapists/profile/janet-lee-20200107', 'https://www.goodtherapy.org/therapists/profile/candice-baugh-20200304', 'https://www.goodtherapy.org/therapists/profile/stephen-horgan-20151026', 'https://www.goodtherapy.org/therapists/profile/amy-wirthnolan-20170317', 'https://www.goodtherapy.org/therapists/profile/abby-grayson-20120914', 'https://www.goodtherapy.org/therapists/profile/annabella-sollaccio-20200422', 'https://www.goodtherapy.org/therapists/profile/linda-jame-20100105', 'https://www.goodtherapy.org/therapists/profile/rachel-perlman-20180522', 'https://www.goodtherapy.org/therapists/profile/laura-okeefe-20081102', 'https://www.goodtherapy.org/therapists/profile/susan-williams-20170128', 'https://www.goodtherapy.org/therapists/profile/rachel-siehs-20180315', 'https://www.goodtherapy.org/therapists/profile/patricia-magnotta-20191115', 'https://www.goodtherapy.org/therapists/profile/judith-margolin-20101027', 'https://www.goodtherapy.org/therapists/profile/tai-pimputkar-20160424', 'https://www.goodtherapy.org/therapists/profile/michele-lucas-20090721', 'https://www.goodtherapy.org/therapists/profile/shira-schaktman-20180326', 'https://www.goodtherapy.org/therapists/profile/pamela-farrell-20110213', 'https://www.goodtherapy.org/therapists/profile/frank-thewes-20180103', 'https://www.goodtherapy.org/therapists/profile/selma-a-sisco-20130417', 'https://www.goodtherapy.org/therapists/profile/sue-sirlin-20191106', 'https://www.goodtherapy.org/therapists/profile/marjorie-demshock-20090301', 'https://www.goodtherapy.org/therapists/profile/rachel-winton-20190314', 'https://www.goodtherapy.org/therapists/profile/john-callahan-20150610', 'https://www.goodtherapy.org/therapists/profile/laurel-levin-20151129', 'https://www.goodtherapy.org/therapists/profile/a-susan-brenner-20120607', 'https://www.goodtherapy.org/therapists/profile/saadia-safian-20190914', 'https://www.goodtherapy.org/therapists/profile/richelle-walling-20180624', 'https://www.goodtherapy.org/therapists/profile/roberta-tessler-20100627', 'https://www.goodtherapy.org/therapists/profile/lori-goldman-20180421', 'https://www.goodtherapy.org/therapists/profile/brianna-conklin-20180923', 'https://www.goodtherapy.org/therapists/profile/carolyn-stout-20181216', 'https://www.goodtherapy.org/therapists/profile/carolanne-hunt-20190309', 'https://www.goodtherapy.org/therapists/profile/margaret-plantes', 'https://www.goodtherapy.org/therapists/profile/deborah-therkorn', 'https://www.goodtherapy.org/therapists/profile/lauren-zavodnick', 'https://www.goodtherapy.org/therapists/profile/Constance-Cloonan', 'https://www.goodtherapy.org/therapists/profile/sangeeta-akundi', 'https://www.goodtherapy.org/therapists/profile/vanessa-hitchman', 'https://www.goodtherapy.org/therapists/profile/jeffrey-kaplan-20130131', 'https://www.goodtherapy.org/therapists/profile/eve-hornstein-20151212', 'https://www.goodtherapy.org/therapists/profile/paula-levy-20100202', 'https://www.goodtherapy.org/therapists/profile/sean-travis', 'https://www.goodtherapy.org/therapists/profile/raquel-jones', 'https://www.goodtherapy.org/therapists/profile/david-king-20160409', 'https://www.goodtherapy.org/therapists/profile/nancy-scherlong-20070410', 'https://www.goodtherapy.org/therapists/profile/jodi-berman-20131223', 'https://www.goodtherapy.org/therapists/profile/joyce-colburn-20150918', 'https://www.goodtherapy.org/therapists/profile/wendy-eisenberg-20101117', 'https://www.goodtherapy.org/therapists/profile/andrew-wagenseller', 'https://www.goodtherapy.org/therapists/profile/mirel-adler-20190611', 'https://www.goodtherapy.org/therapists/profile/amy-cargill-20190613', 'https://www.goodtherapy.org/therapists/profile/leo-battenhausen-20190816', 'https://www.goodtherapy.org/therapists/profile/ruth-altamuraroll-20140120', 'https://www.goodtherapy.org/therapists/profile/randi-cohen-20150722', 'https://www.goodtherapy.org/therapists/profile/gwendolyn-blake-20170815', 'https://www.goodtherapy.org/therapists/profile/leticia-vitucci-20190514', 'https://www.goodtherapy.org/therapists/profile/jamie-vollmoeller-20190627', 'https://www.goodtherapy.org/therapists/profile/stefanie-stadler-20190713', 'https://www.goodtherapy.org/therapists/profile/belle-lopes-20181028', 'https://www.goodtherapy.org/therapists/profile/danna-anderson-20200326', 'https://www.goodtherapy.org/therapists/profile/yvonne-bregman-20101027', 'https://www.goodtherapy.org/therapists/profile/susan-polese-20161102', 'https://www.goodtherapy.org/therapists/profile/kelley-hopkinsalvarez-20110913', 'https://www.goodtherapy.org/therapists/profile/nicole-steen-20170718', 'https://www.goodtherapy.org/therapists/profile/kimberly-hession-20170714', 'https://www.goodtherapy.org/therapists/profile/christine-colavito-20171009', 'https://www.goodtherapy.org/therapists/profile/matthew-love-20190421', 'https://www.goodtherapy.org/therapists/profile/tamara-pommells-20130322', 'https://www.goodtherapy.org/therapists/profile/rhonda-loft-20130211', 'https://www.goodtherapy.org/therapists/profile/nicole-commercio-20180105', 'https://www.goodtherapy.org/therapists/profile/mary-goepfert-20191020', 'https://www.goodtherapy.org/therapists/profile/kara-yass-20190829', 'https://www.goodtherapy.org/therapists/profile/jodie-rinde-20200119', 'https://www.goodtherapy.org/therapists/profile/robby-foster-20180525', 'https://www.goodtherapy.org/therapists/profile/amy-wohl-20140519', 'https://www.goodtherapy.org/therapists/profile/cynthia-fischer-20130306', 'https://www.goodtherapy.org/therapists/profile/laura-van-schaickharman-20120718', 'https://www.goodtherapy.org/therapists/profile/amy-negri-20170830', 'https://www.goodtherapy.org/therapists/profile/alicia-williams-20200409', 'https://www.goodtherapy.org/therapists/profile/neil-klatsky-20180425', 'https://www.goodtherapy.org/therapists/profile/marcos-rosa-20200301', 'https://www.goodtherapy.org/therapists/profile/morgan-burgess-20140724', 'https://www.goodtherapy.org/therapists/profile/amie-markowitz-20121018', 'https://www.goodtherapy.org/therapists/profile/deja-harford-20171206', 'https://www.goodtherapy.org/therapists/profile/lori-capri-20170624', 'https://www.goodtherapy.org/therapists/profile/jacqueline-dudas-20180424', 'https://www.goodtherapy.org/therapists/profile/rachel-coombs-20180911', 'https://www.goodtherapy.org/therapists/profile/christine-lynch-20191102', 'https://www.goodtherapy.org/therapists/profile/joanne-martin-20190511', 'https://www.goodtherapy.org/therapists/profile/celeste-aliberti-20170424', 'https://www.goodtherapy.org/therapists/profile/elizabeth-cruickshank-20150205', 'https://www.goodtherapy.org/therapists/profile/danielle-sangalli-20151106', 'https://www.goodtherapy.org/therapists/profile/laura-chiusano-20191018', 'https://www.goodtherapy.org/therapists/profile/christine-etzrodt-20180205', 'https://www.goodtherapy.org/therapists/profile/david-piltz-20171004', 'https://www.goodtherapy.org/therapists/profile/mary-anne-fielding-20140204', 'https://www.goodtherapy.org/therapists/profile/janet-cunningham-20170512', 'https://www.goodtherapy.org/therapists/profile/brianna-fava-20121017', 'https://www.goodtherapy.org/therapists/profile/mary-shull-20140929', 'https://www.goodtherapy.org/therapists/profile/judith-barr-20080716', 'https://www.goodtherapy.org/therapists/profile/randy-w-green-20110310', 'https://www.goodtherapy.org/therapists/profile/prunella-harris-20200114', 'https://www.goodtherapy.org/therapists/profile/elisabeth-burrelli-20140208', 'https://www.goodtherapy.org/therapists/profile/eric-jackson-20140316', 'https://www.goodtherapy.org/therapists/profile/carmen-garrison-20140922', 'https://www.goodtherapy.org/therapists/profile/joyce-cooney-20200407', 'https://www.goodtherapy.org/therapists/profile/stacee-paley-20190827', 'https://www.goodtherapy.org/therapists/profile/emily-easterling-20170403', 'https://www.goodtherapy.org/therapists/profile/lavanya-devdas-20190611', 'https://www.goodtherapy.org/therapists/profile/kristen-marsarperez-20140629', 'https://www.goodtherapy.org/therapists/profile/meghan-jerry-20161012', 'https://www.goodtherapy.org/therapists/profile/kevin-drab-20120406', 'https://www.goodtherapy.org/therapists/profile/stephen-britchkow-20120228', 'https://www.goodtherapy.org/therapists/profile/erica-holtz-20130923', 'https://www.goodtherapy.org/therapists/profile/susan-krauss-20130904', 'https://www.goodtherapy.org/therapists/profile/wendy-blair-20120129', 'https://www.goodtherapy.org/therapists/profile/kelly-reed-20150917', 'https://www.goodtherapy.org/therapists/profile/dori-kovacs-20190327', 'https://www.goodtherapy.org/therapists/profile/linda-hill-20070826', 'https://www.goodtherapy.org/therapists/profile/persida-ghibilic-20141123', 'https://www.goodtherapy.org/therapists/profile/charmaine-samuda-20190607', 'https://www.goodtherapy.org/therapists/profile/thomas-reilly-20160117', 'https://www.goodtherapy.org/therapists/profile/lucrezia-mangione-20131029', 'https://www.goodtherapy.org/therapists/profile/ellen-faulkner-20130803', 'https://www.goodtherapy.org/therapists/profile/thomas-blackwell-20160413', 'https://www.goodtherapy.org/therapists/profile/meredith-messinger-20190309', 'https://www.goodtherapy.org/therapists/profile/kaitlyn-russell-20190315', 'https://www.goodtherapy.org/therapists/profile/tara-reynolds', 'https://www.goodtherapy.org/therapists/profile/Jaime-Benedetti', 'https://www.goodtherapy.org/therapists/profile/elizabeth-deboer-kreider-20150915', 'https://www.goodtherapy.org/therapists/profile/gina-rossini-20151216', 'https://www.goodtherapy.org/therapists/profile/m-catherine-ambrose-20141120', 'https://www.goodtherapy.org/therapists/profile/rowan-moore-20150508', 'https://www.goodtherapy.org/therapists/profile/stacey-vinci-20200406', 'https://www.goodtherapy.org/therapists/profile/ellen-schrier-20130716', 'https://www.goodtherapy.org/therapists/profile/howard-ratner-20181024', 
# 'https://www.goodtherapy.org/therapists/profile/karen-wister-kearns-20190902', 'https://www.goodtherapy.org/therapists/profile/rusty-stewart-phd-20110831', 'https://www.goodtherapy.org/therapists/profile/joan-cybulski-20161229', 'https://www.goodtherapy.org/therapists/profile/angela-kurzyna-20200318', 'https://www.goodtherapy.org/therapists/profile/molly-guest-20171005', 'https://www.goodtherapy.org/therapists/profile/jennifer-matthes-20200508', 'https://www.goodtherapy.org/therapists/profile/jill-harle-20140916', 'https://www.goodtherapy.org/therapists/profile/elizabeth-casey-20160316', 'https://www.goodtherapy.org/therapists/profile/alexis-ledner-20190824', 'https://www.goodtherapy.org/therapists/profile/rebecca-kornberg-20190901', 'https://www.goodtherapy.org/therapists/profile/lori-christine-young-20140611', 'https://www.goodtherapy.org/therapists/profile/eugene-kayser-20160524', 'https://www.goodtherapy.org/therapists/profile/robert-smith-20171201', 'https://www.goodtherapy.org/therapists/profile/victoria-sayles-20100109', 'https://www.goodtherapy.org/therapists/profile/rhoda-fuchsmorton-20091116', 'https://www.goodtherapy.org/therapists/profile/james-baldwin-20120508', 'https://www.goodtherapy.org/therapists/profile/renee-friersonbriscoe-20170505', 'https://www.goodtherapy.org/therapists/profile/stephen-sell-20190304', 'https://www.goodtherapy.org/therapists/profile/francine-roberts-20150207', 'https://www.goodtherapy.org/therapists/profile/jeffrey-carter-20140930', 'https://www.goodtherapy.org/therapists/profile/jeannine-coyne-20180212', 'https://www.goodtherapy.org/therapists/profile/taniek-gentles-20191010', 'https://www.goodtherapy.org/therapists/profile/raul-avila-20150417', 'https://www.goodtherapy.org/therapists/profile/gabrielle-morreale-20191111', 'https://www.goodtherapy.org/therapists/profile/david-leibovitz-20100929', 'https://www.goodtherapy.org/therapists/profile/rashun-stewart-20160906', 'https://www.goodtherapy.org/therapists/profile/jason-cohen-20190301', 'https://www.goodtherapy.org/therapists/profile/meg-clark-soriano-20141011', 'https://www.goodtherapy.org/therapists/profile/janeen-cross-20200317', 'https://www.goodtherapy.org/therapists/profile/todd-koser-20170716', 'https://www.goodtherapy.org/therapists/profile/Yamillis-Hernandez', 'https://www.goodtherapy.org/therapists/profile/tammy-henderson', 'https://www.goodtherapy.org/therapists/profile/peter-golboro-20180911', 'https://www.goodtherapy.org/therapists/profile/jasmin-rahman-20180414', 'https://www.goodtherapy.org/therapists/profile/allison-macher-20180610', 'https://www.goodtherapy.org/therapists/profile/bonnie-stevens-20180610', 'https://www.goodtherapy.org/therapists/profile/michael-haas-20180610', 'https://www.goodtherapy.org/therapists/profile/rosemary-williams-20190131', 'https://www.goodtherapy.org/therapists/profile/jen-perry-20141129', 'https://www.goodtherapy.org/therapists/profile/annie-fisher-20190917', 'https://www.goodtherapy.org/therapists/profile/lyn-felix-20110201', 'https://www.goodtherapy.org/therapists/profile/daniel-gottlieb-20090728', 'https://www.goodtherapy.org/therapists/profile/randy-carrin-20090707', 'https://www.goodtherapy.org/therapists/profile/lucy-s-raizman-20161020', 'https://www.goodtherapy.org/therapists/profile/emily-masko-20191201', 'https://www.goodtherapy.org/therapists/profile/william-dewart-20120416', 'https://www.goodtherapy.org/therapists/profile/willie-knight-20160901', 'https://www.goodtherapy.org/therapists/profile/kaitlin-staples-20190522', 'https://www.goodtherapy.org/therapists/profile/deidre-ashton-20150219', 'https://www.goodtherapy.org/therapists/profile/ellen-piper-20130312', 'https://www.goodtherapy.org/therapists/profile/amanda-haidet-20200407', 'https://www.goodtherapy.org/therapists/profile/helena-w-king-20190207', 'https://www.goodtherapy.org/therapists/profile/earl-lewis-20200403', 'https://www.goodtherapy.org/therapists/profile/julia-markovitz-20181119', 'https://www.goodtherapy.org/therapists/profile/iolanda-marucci-20161116', 'https://www.goodtherapy.org/therapists/profile/david-steinberg-20111129', 'https://www.goodtherapy.org/therapists/profile/marla-cohen-20130306', 'https://www.goodtherapy.org/therapists/profile/leah-behl-20140807', 'https://www.goodtherapy.org/therapists/profile/leana-sykes-20140619', 'https://www.goodtherapy.org/therapists/profile/amy-kasten-20110518', 'https://www.goodtherapy.org/therapists/profile/carolynn-aristone-20080317', 'https://www.goodtherapy.org/therapists/profile/amy-kempe-20171129', 'https://www.goodtherapy.org/therapists/profile/barry-lessin-20110822', 'https://www.goodtherapy.org/therapists/profile/katherine-schneider-20191007', 'https://www.goodtherapy.org/therapists/profile/marquita-bolden-20130221', 'https://www.goodtherapy.org/therapists/profile/jessica-getson-20170125', 'https://www.goodtherapy.org/therapists/profile/philip-friedman-20100827', 'https://www.goodtherapy.org/therapists/profile/colleen-fitzpatrick-20150407', 'https://www.goodtherapy.org/therapists/profile/tracy-clough-20180122', 'https://www.goodtherapy.org/therapists/profile/ashley-baldwin-20171130', 'https://www.goodtherapy.org/therapists/profile/yong-lee-20180102', 'https://www.goodtherapy.org/therapists/profile/susan-rosenberg-20150319', 'https://www.goodtherapy.org/therapists/profile/maria-pandolfi-20200426', 'https://www.goodtherapy.org/therapists/profile/rita-garcia-20170109', 'https://www.goodtherapy.org/therapists/profile/maureen-fiorelli-20090518', 'https://www.goodtherapy.org/therapists/profile/josh-dodes-20150909', 'https://www.goodtherapy.org/therapists/profile/harold-kirby-20130223', 'https://www.goodtherapy.org/therapists/profile/casey-mccollum-20200103', 'https://www.goodtherapy.org/therapists/profile/sonya-kearney-20190821', 'https://www.goodtherapy.org/therapists/profile/hope-nichols-20150426', 'https://www.goodtherapy.org/therapists/profile/jeremy-frank-20091031', 'https://www.goodtherapy.org/therapists/profile/ruth-conviser-20190801', 'https://www.goodtherapy.org/therapists/profile/timothy-walsh-20170802', 'https://www.goodtherapy.org/therapists/profile/richard-brewer-20110601', 'https://www.goodtherapy.org/therapists/profile/marcus-krohner-20181009', 'https://www.goodtherapy.org/therapists/profile/erin-obrien-20110718', 'https://www.goodtherapy.org/therapists/profile/danielle-adinolfi-20161115', 'https://www.goodtherapy.org/therapists/profile/amy-scarano-20190401', 'https://www.goodtherapy.org/therapists/profile/elise-gaul-20160406', 'https://www.goodtherapy.org/therapists/profile/marram-emily-jane-plapp-20170204', 'https://www.goodtherapy.org/therapists/profile/julie-sponsler-20080205', 'https://www.goodtherapy.org/therapists/profile/margaret-hogan-20090109', 'https://www.goodtherapy.org/therapists/profile/ellen-ostroff-20190701', 'https://www.goodtherapy.org/therapists/profile/marcia-polansky-20080920', 'https://www.goodtherapy.org/therapists/profile/katrina-pinkney-20190309', 'https://www.goodtherapy.org/therapists/profile/michael-bernstein-20190305', 'https://www.goodtherapy.org/therapists/profile/sarah-hildebrand-20190515', 'https://www.goodtherapy.org/therapists/profile/nicola-pierresmith-20200101', 'https://www.goodtherapy.org/therapists/profile/craig-cohen-20130603', 'https://www.goodtherapy.org/therapists/profile/jacqueline-falkenheim-20130101', 'https://www.goodtherapy.org/therapists/profile/walter-matweychuk-20140104', 'https://www.goodtherapy.org/therapists/profile/lindsay-bauer-20150114', 'https://www.goodtherapy.org/therapists/profile/marie-papalia-20190201', 'https://www.goodtherapy.org/therapists/profile/jennifer-bullock-20080116', 'https://www.goodtherapy.org/therapists/profile/perri-shaw-borish-20071013', 'https://www.goodtherapy.org/therapists/profile/jill-lipschutz-snyder-20090404', 'https://www.goodtherapy.org/therapists/profile/chris-fariello-20160913', 'https://www.goodtherapy.org/therapists/profile/medb-mcgearty-20140218', 'https://www.goodtherapy.org/therapists/profile/marion-rudin-frank-20120930', 'https://www.goodtherapy.org/therapists/profile/josh-zlatkus-20170507', 'https://www.goodtherapy.org/therapists/profile/julie-present-koller-20190223', 'https://www.goodtherapy.org/therapists/profile/inger-colzie-20150412', 'https://www.goodtherapy.org/therapists/profile/carol-schaefer-20110407', 'https://www.goodtherapy.org/therapists/profile/audrey-morrow-20130111', 'https://www.goodtherapy.org/therapists/profile/alison-dye-20110618', 'https://www.goodtherapy.org/therapists/profile/linda-spero-20110221', 'https://www.goodtherapy.org/therapists/profile/andrew-matusiak-20190617', 'https://www.goodtherapy.org/therapists/profile/wanda-sevey-20160715', 'https://www.goodtherapy.org/therapists/profile/nancy-macgregor-20200429', 'https://www.goodtherapy.org/therapists/profile/diana-cofsky', 'https://www.goodtherapy.org/therapists/profile/jennifer-adamski', 'https://www.goodtherapy.org/therapists/profile/caroline-chait-20191112', 'https://www.goodtherapy.org/therapists/profile/carole-landis-20121230', 'https://www.goodtherapy.org/therapists/profile/allison-bogdanoff-20170123', 'https://www.goodtherapy.org/therapists/profile/ashley-cook-20140101', 'https://www.goodtherapy.org/therapists/profile/tasnim-sulaiman-20140712', 'https://www.goodtherapy.org/therapists/profile/morton-axelrod-20090707', 'https://www.goodtherapy.org/therapists/profile/kristina-ferrari-20190203', 'https://www.goodtherapy.org/therapists/profile/dina-harth-20150922', 'https://www.goodtherapy.org/therapists/profile/arlene-foreman-20140509', 'https://www.goodtherapy.org/therapists/profile/patricia-constantinian-20180705', 'https://www.goodtherapy.org/therapists/profile/dorothy-winrow-20120925', 'https://www.goodtherapy.org/therapists/profile/persa-delapp-20181220', 'https://www.goodtherapy.org/therapists/profile/jed-yalof-20151031', 'https://www.goodtherapy.org/therapists/profile/sarah-murphy-20181001', 
# 'https://www.goodtherapy.org/therapists/profile/brian-berman-20150211', 'https://www.goodtherapy.org/therapists/profile/dawn-altman-20191113', 'https://www.goodtherapy.org/therapists/profile/jeffrey-cox-20200520', 'https://www.goodtherapy.org/therapists/profile/safieh-kash-20170905', 'https://www.goodtherapy.org/therapists/profile/eileen-jason-phd-20170906', 'https://www.goodtherapy.org/therapists/profile/melissa-mclean-20171205', 'https://www.goodtherapy.org/therapists/profile/brian-stemetzki-20150904', 'https://www.goodtherapy.org/therapists/profile/charles-zeiders-20160412', 'https://www.goodtherapy.org/therapists/profile/karen-ognibene-20170127', 'https://www.goodtherapy.org/therapists/profile/kathryn-burnett-20180830', 'https://www.goodtherapy.org/therapists/profile/jacquelynn-cunliffe-20100523', 'https://www.goodtherapy.org/therapists/profile/debra-nelson-20120909', 'https://www.goodtherapy.org/therapists/profile/stacia-bjarnason-20190402', 'https://www.goodtherapy.org/therapists/profile/john-novielli-20140221', 'https://www.goodtherapy.org/therapists/profile/jan-blumenthal-20150615', 'https://www.goodtherapy.org/therapists/profile/john-rex-20121206', 'https://www.goodtherapy.org/therapists/profile/john-mondello-20101027', 'https://www.goodtherapy.org/therapists/profile/christine-bishopedkins-20180627', 'https://www.goodtherapy.org/therapists/profile/meg-schneider-20200428', 'https://www.goodtherapy.org/therapists/profile/bridgette-montgomery-20150601', 'https://www.goodtherapy.org/therapists/profile/heather-vargo-20160913', 'https://www.goodtherapy.org/therapists/profile/scott-giacomucci-20191208', 'https://www.goodtherapy.org/therapists/profile/mary-deitch-20151209', 'https://www.goodtherapy.org/therapists/profile/sarah-tolvaisa-20180901', 'https://www.goodtherapy.org/therapists/profile/dwight-norwood-20160207', 'https://www.goodtherapy.org/therapists/profile/jeannette-lofas-20160908', 'https://www.goodtherapy.org/therapists/profile/stephanie-menta-20191017', 'https://www.goodtherapy.org/therapists/profile/sherry-osadchey-20071108', 'https://www.goodtherapy.org/therapists/profile/joel-kaye-20100609', 'https://www.goodtherapy.org/therapists/profile/renee-balthrop-20170926', 'https://www.goodtherapy.org/therapists/profile/neil-becker-20140513', 'https://www.goodtherapy.org/therapists/profile/kanjana-hartshorne-20171006', 'https://www.goodtherapy.org/therapists/profile/paula-tropiano-20140410', 'https://www.goodtherapy.org/therapists/profile/matthew-gelber-20080207', 'https://www.goodtherapy.org/therapists/profile/randall-dwenger-20190913', 'https://www.goodtherapy.org/therapists/profile/dr-soraya-sawicki-lcsw-20191124', 'https://www.goodtherapy.org/therapists/profile/janet-edgette-20101221', 'https://www.goodtherapy.org/therapists/profile/christine-brunetti-20140516', 'https://www.goodtherapy.org/therapists/profile/karen-fraley-20170213', 'https://www.goodtherapy.org/therapists/profile/ronald-sabadish-20170715', 'https://www.goodtherapy.org/therapists/profile/eileen-stecker-20090107', 'https://www.goodtherapy.org/therapists/profile/lori-carpenos-20110306', 'https://www.goodtherapy.org/therapists/profile/joshua-cohen-20181025', 'https://www.goodtherapy.org/therapists/profile/jessica-assardwu-20100116', 'https://www.goodtherapy.org/therapists/profile/bryon-remo-20161013', 'https://www.goodtherapy.org/therapists/profile/michael-jody-20130930', 'https://www.goodtherapy.org/therapists/profile/elliott-strick-20110615', 'https://www.goodtherapy.org/therapists/profile/nowakowski-terry-20200220', 'https://www.goodtherapy.org/therapists/profile/kate-destefanotorres-20160113', 'https://www.goodtherapy.org/therapists/profile/maria-gabelberger-20140715', 'https://www.goodtherapy.org/therapists/profile/andrew-burkamp-20151016', 'https://www.goodtherapy.org/therapists/profile/erik-young-20110706', 'https://www.goodtherapy.org/therapists/profile/kristina-chomick-20150518', 'https://www.goodtherapy.org/therapists/profile/shelby-riley-20110905', 'https://www.goodtherapy.org/therapists/profile/nancy-depaul-20140302', 'https://www.goodtherapy.org/therapists/profile/lisa-brugger-20110905', 'https://www.goodtherapy.org/therapists/profile/nancy-brockett-20110121', 'https://www.goodtherapy.org/therapists/profile/angeles-ramos-20181023', 'https://www.goodtherapy.org/therapists/profile/peggy-phipps-20151123', 'https://www.goodtherapy.org/therapists/profile/john-obell-20190730', 'https://www.goodtherapy.org/therapists/profile/nicole-lewis-20170811', 'https://www.goodtherapy.org/therapists/profile/taryn-sharkey-20200117', 'https://www.goodtherapy.org/therapists/profile/egypciel-victorlowderback-20111111', 
# 'https://www.goodtherapy.org/therapists/profile/adam-bernstein-20200316']

# pickle.dump(ls, open( "nyc_links_leftovers_1.pkl", "wb" ) )