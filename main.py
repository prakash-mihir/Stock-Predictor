import streamlit as st
from datetime import date
import pandas as pd
import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go

START = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

st.title('Stock Forecast App')

stocks = ('20MICRONS.NS', 
'21STCENMGM.NS', 
'3IINFOLTD.NS', 
'3MINDIA.NS', 
'3PLAND.NS', 
'3RDROCK.NS', 
'4THDIM.NS', 
'5PAISA.NS', 
'63MOONS.NS', 
'A2ZINFRA.NS', 
'AAATECH.NS', 
'AAKASH.NS', 
'AAREYDRUGS.NS', 
'AARON.NS', 
'AARTIDRUGS.NS', 
'AARTIIND.NS', 
'AARTISURF.NS', 
'AARVEEDEN.NS', 
'AARVI.NS', 
'AAVAS.NS', 
'ABAN.NS', 
'ABB.NS', 
'ABCAPITAL.NS', 
'ABCOTS.NS', 
'ABFRL.NS', 
'ABHISHEK.NS', 
'ABINFRA.NS', 
'ABMINTLLTD.NS', 
'ABNINT.NS', 
'ABSLAMC.NS', 
'ACC.NS', 
'ACCELYA.NS', 
'ACCORD.NS', 
'ACCURACY.NS', 
'ACE.NS', 
'ACEINTEG.NS', 
'ACI.NS', 
'ADANIENT.NS', 
'ADANIGREEN.NS', 
'ADANIPORTS.NS', 
'ADANIPOWER.NS', 
'ADANITRANS.NS', 
'ADFFOODS.NS', 
'ADL.NS', 
'ADORWELD.NS', 
'ADROITINFO.NS', 
'ADSL.NS', 
'ADVANIHOTR.NS', 
'ADVENZYMES.NS', 
'AEGISCHEM.NS', 
'AETHER.NS', 
'AFFLE.NS', 
'AGARIND.NS', 
'AGI.NS', 
'AGNI.NS', 
'AGRITECH.NS', 
'AGROPHOS.NS', 
'AGSTRA.NS', 
'AHIMSA.NS', 
'AHL.NS', 
'AHLADA.NS', 
'AHLEAST.NS', 
'AHLUCONT.NS', 
'AHLWEST.NS', 
'AIAENG.NS', 
'AIFL.NS', 
'AILIMITED.NS', 
'AIRAN.NS', 
'AIROLAM.NS', 
'AISL.NS', 
'AJANTPHARM.NS', 
'AJMERA.NS', 
'AJOONI.NS', 
'AJRINFRA.NS', 
'AKASH.NS', 
'AKG.NS', 
'AKSHAR.NS', 
'AKSHARCHEM.NS', 
'AKSHOPTFBR.NS', 
'AKZOINDIA.NS', 
'ALANKIT.NS', 
'ALBERTDAVD.NS', 
'ALCHEM.NS', 
'ALEMBICLTD.NS', 
'ALICON.NS', 
'ALKALI.NS', 
'ALKEM.NS', 
'ALKYLAMINE.NS', 
'ALLCARGO.NS', 
'ALLETEC.NS', 
'ALLSEC.NS', 
'ALMONDZ.NS', 
'ALOKINDS.NS', 
'ALPA.NS', 
'ALPHAGEO.NS', 
'ALPSINDUS.NS', 
'AMARAJABAT.NS', 
'AMBANIORG.NS', 
'AMBER.NS', 
'AMBICAAGAR.NS', 
'AMBIKCO.NS', 
'AMBUJACEM.NS', 
'AMDIND.NS', 
'AMEYA.NS', 
'AMIABLE.NS', 
'AMIORG.NS', 
'AMJLAND.NS', 
'AMJUMBO.NS', 
'AMRUTANJAN.NS', 
'ANANDRATHI.NS', 
'ANANTRAJ.NS', 
'ANDHRACEMT.NS', 
'ANDHRAPAP.NS', 
'ANDHRSUGAR.NS', 
'ANGELONE.NS', 
'ANIKINDS.NS', 
'ANKITMETAL.NS', 
'ANMOL.NS', 
'ANNAPURNA.NS', 
'ANSALAPI.NS', 
'ANTGRAPHIC.NS', 
'ANUP.NS', 
'ANURAS.NS', 
'APARINDS.NS', 
'APCL.NS', 
'APCOTEXIND.NS', 
'APEX.NS', 
'APLAPOLLO.NS', 
'APLLTD.NS', 
'APOLLO.NS', 
'APOLLOHOSP.NS', 
'APOLLOPIPE.NS', 
'APOLLOTYRE.NS', 
'APOLSINHOT.NS', 
'APTECHT.NS', 
'APTUS.NS', 
'ARCHIDPLY.NS', 
'ARCHIES.NS', 
'ARCOTECH.NS', 
'ARENTERP.NS', 
'ARHAM.NS', 
'ARIES.NS', 
'ARIHANTACA.NS', 
'ARIHANTCAP.NS', 
'ARIHANTSUP.NS', 
'ARMANFIN.NS', 
'AROGRANITE.NS', 
'ARROWGREEN.NS', 
'ARSHIYA.NS', 
'ARSSINFRA.NS', 
'ARTEDZ.NS', 
'ARTEMISMED.NS', 
'ARTNIRMAN.NS', 
'ARVEE.NS', 
'ARVIND.NS', 
'ARVINDFASN.NS', 
'ARVSMART.NS', 
'ASAHIINDIA.NS', 
'ASAHISONG.NS', 
'ASAL.NS', 
'ASALCBR.NS', 
'ASCOM.NS', 
'ASHAPURMIN.NS', 
'ASHIANA.NS', 
'ASHIMASYN.NS', 
'ASHOKA.NS', 
'ASHOKLEY.NS', 
'ASIANENE.NS', 
'ASIANHOTNR.NS', 
'ASIANPAINT.NS', 
'ASIANTILES.NS', 
'ASIL.NS', 
'ASLIND.NS', 
'ASPINWALL.NS', 
'ASTEC.NS', 
'ASTERDM.NS', 
'ASTRAL.NS', 
'ASTRAMICRO.NS', 
'ASTRAZEN.NS', 
'ASTRON.NS', 
'ATALREAL.NS', 
'ATCOM.NS', 
'ATFL.NS', 
'ATGL.NS', 
'ATLANTA.NS', 
'ATLASCYCLE.NS', 
'ATNINTER.NS', 
'ATUL.NS', 
'ATULAUTO.NS', 
'AUBANK.NS', 
'AURDIS.NS', 
'AURIONPRO.NS', 
'AUROPHARMA.NS', 
'AURUM.NS', 
'AUSOMENT.NS', 
'AUTOAXLES.NS', 
'AUTOIND.NS', 
'AUTOLITIND.NS', 
'AUTORIDFIN.NS', 
'AVADHSUGAR.NS', 
'AVANTIFEED.NS', 
'AVG.NS', 
'AVROIND.NS', 
'AVSL.NS', 
'AVTNPL.NS', 
'AWHCL.NS', 
'AWL.NS', 
'AXISBANK.NS', 
'AXISCADES.NS', 
'AXITA.NS', 
'AYMSYNTEX.NS', 
'BAFNAPH.NS', 
'BAGFILMS.NS', 
'BAHETI.NS', 
'BAJAJ-AUTO.NS', 
'BAJAJCON.NS', 
'BAJAJELEC.NS', 
'BAJAJFINSV.NS', 
'BAJAJHCARE.NS', 
'BAJAJHIND.NS', 
'BAJAJHLDNG.NS', 
'BAJFINANCE.NS', 
'BALAJITELE.NS', 
'BALAMINES.NS', 
'BALAXI.NS', 
'BALKRISHNA.NS', 
'BALKRISIND.NS', 
'BALLARPUR.NS', 
'BALMLAWRIE.NS', 
'BALPHARMA.NS', 
'BALRAMCHIN.NS', 
'BANARBEADS.NS', 
'BANARISUG.NS', 
'BANCOINDIA.NS', 
'BANDHANBNK.NS', 
'BANG.NS', 
'BANKA.NS', 
'BANKBARODA.NS', 
'BANKINDIA.NS', 
'BANSAL.NS', 
'BANSWRAS.NS', 
'BARBEQUE.NS', 
'BARTRONICS.NS', 
'BASF.NS', 
'BASML.NS', 
'BATAINDIA.NS', 
'BBL.NS', 
'BBOX.NS', 
'BBTC.NS', 
'BBTCL.NS', 
'BCG.NS', 
'BCLIND.NS', 
'BCONCEPTS.NS', 
'BDL.NS', 
'BDR.NS', 
'BEARDSELL.NS', 
'BECTORFOOD.NS', 
'BEDMUTHA.NS', 
'BEL.NS', 
'BEML.NS', 
'BEPL.NS', 
'BERGEPAINT.NS', 
'BETA.NS', 
'BEWLTD.NS', 
'BFINVEST.NS', 
'BFUTILITIE.NS', 
'BGLOBAL.NS', 
'BGRENERGY.NS', 
'BHAGCHEM.NS', 
'BHAGERIA.NS', 
'BHAGYANGR.NS', 
'BHALCHANDR.NS', 
'BHANDARI.NS', 
'BHARATFORG.NS', 
'BHARATGEAR.NS', 
'BHARATIDIL.NS', 
'BHARATRAS.NS', 
'BHARATWIRE.NS', 
'BHARTIARTL.NS', 
'BHEL.NS', 
'BIGBLOC.NS', 
'BIKAJI.NS', 
'BIL.NS', 
'BILENERGY.NS', 
'BINANIIND.NS', 
'BINDALAGRO.NS', 
'BIOCON.NS', 
'BIOFILCHEM.NS', 
'BIRLACABLE.NS', 
'BIRLACORPN.NS', 
'BIRLAMONEY.NS', 
'BIRLATYRE.NS', 
'BKMINDST.NS', 
'BLBLIMITED.NS', 
'BLISSGVS.NS', 
'BLKASHYAP.NS', 
'BLS.NS', 
'BLUEBLENDS.NS', 
'BLUECHIP.NS', 
'BLUECOAST.NS', 
'BLUEDART.NS', 
'BLUESTARCO.NS', 
'BMETRICS.NS', 
'BODALCHEM.NS', 
'BOHRAIND.NS', 
'BOMDYEING.NS', 
'BOROLTD.NS', 
'BORORENEW.NS', 
'BOSCHLTD.NS', 
'BPCL.NS', 
'BPL.NS', 
'BRFL.NS', 
'BRIGADE.NS', 
'BRIGHT.NS', 
'BRITANNIA.NS', 
'BRNL.NS', 
'BROOKS.NS', 
'BSE.NS', 
'BSHSL.NS', 
'BSL.NS', 
'BSOFT.NS', 
'BTML.NS', 
'BURNPUR.NS', 
'BUTTERFLY.NS', 
'BVCL.NS', 
'BYKE.NS', 
'CADSYS.NS', 
'CALSOFT.NS', 
'CAMLINFINE.NS', 
'CAMPUS.NS', 
'CAMS.NS', 
'CANBK.NS', 
'CANDC.NS', 
'CANFINHOME.NS', 
'CANTABIL.NS', 
'CAPACITE.NS', 
'CAPLIPOINT.NS', 
'CAPTRUST.NS', 
'CARBORUNIV.NS', 
'CAREERP.NS', 
'CARERATING.NS', 
'CARTRADE.NS', 
'CARYSIL.NS', 
'CASTROLIND.NS', 
'CCCL.NS', 
'CCHHL.NS', 
'CCL.NS', 
'CDSL.NS', 
'CEATLTD.NS', 
'CELEBRITY.NS', 
'CELESTIAL.NS', 
'CENTENKA.NS', 
'CENTEXT.NS', 
'CENTRALBK.NS', 
'CENTRUM.NS', 
'CENTUM.NS', 
'CENTURYPLY.NS', 
'CENTURYTEX.NS', 
'CERA.NS', 
'CEREBRAINT.NS', 
'CESC.NS', 
'CGCL.NS', 
'CGPOWER.NS', 
'CHALET.NS', 
'CHAMBLFERT.NS', 
'CHEMBOND.NS', 
'CHEMCON.NS', 
'CHEMFAB.NS', 
'CHEMPLASTS.NS', 
'CHENNPETRO.NS', 
'CHEVIOT.NS', 
'CHOICEIN.NS', 
'CHOLAFIN.NS', 
'CHOLAHLDNG.NS', 
'CIGNITITEC.NS', 
'CINELINE.NS', 
'CINEVISTA.NS', 
'CIPLA.NS', 
'CKFSL.NS', 
'CKPLEISURE.NS', 
'CLEAN.NS', 
'CLEDUCATE.NS', 
'CLNINDIA.NS', 
'CLOUD.NS', 
'CLSEL.NS', 
'CMICABLES.NS', 
'CMMIPL.NS', 
'CMRSL.NS', 
'CMSINFO.NS', 
'COALINDIA.NS', 
'COASTCORP.NS', 
'COCHINSHIP.NS', 
'COFFEEDAY.NS', 
'COFORGE.NS', 
'COLPAL.NS', 
'COMPINFO.NS', 
'COMPUSOFT.NS', 
'CONCOR.NS', 
'CONFIPET.NS', 
'CONSOFINVT.NS', 
'CONTI.NS', 
'CONTROLPR.NS', 
'COOLCAPS.NS', 
'CORALFINAC.NS', 
'CORDSCABLE.NS', 
'COROMANDEL.NS', 
'COSMOFIRST.NS', 
'COUNCODOS.NS', 
'COX&KINGS.NS', 
'CRAFTSMAN.NS', 
'CREATIVE.NS', 
'CREATIVEYE.NS', 
'CREDITACC.NS', 
'CREST.NS', 
'CRISIL.NS', 
'CROMPTON.NS', 
'CROWN.NS', 
'CSBBANK.NS', 
'CSLFINANCE.NS', 
'CTE.NS', 
'CUB.NS', 
'CUBEXTUB.NS', 
'CUMMINSIND.NS', 
'CUPID.NS', 
'CYBERMEDIA.NS', 
'CYBERTECH.NS', 
'CYIENT.NS', 
'DAAWAT.NS', 
'DABUR.NS', 
'DALBHARAT.NS', 
'DALMIASUG.NS', 
'DAMODARIND.NS', 
'DANGEE.NS', 
'DATAMATICS.NS', 
'DATAPATTNS.NS', 
'DBCORP.NS', 
'DBL.NS', 
'DBOL.NS', 
'DBREALTY.NS', 
'DBSTOCKBRO.NS', 
'DCAL.NS', 
'DCBBANK.NS', 
'DCI.NS', 
'DCM.NS', 
'DCMFINSERV.NS', 
'DCMNVL.NS', 
'DCMSHRIRAM.NS', 
'DCMSRIND.NS', 
'DCW.NS', 
'DCXINDIA.NS', 
'DECCANCE.NS', 
'DEEPAKFERT.NS', 
'DEEPAKNTR.NS', 
'DEEPENR.NS', 
'DEEPINDS.NS', 
'DELHIVERY.NS', 
'DELPHIFX.NS', 
'DELTACORP.NS', 
'DELTAMAGNT.NS', 
'DEN.NS', 
'DENORA.NS', 
'DESTINY.NS', 
'DEVIT.NS', 
'DEVYANI.NS', 
'DFMFOODS.NS', 
'DGCONTENT.NS', 
'DHAMPURSUG.NS', 
'DHANBANK.NS', 
'DHANI.NS', 
'DHANUKA.NS', 
'DHARMAJ.NS', 
'DHARSUGAR.NS', 
'DHRUV.NS', 
'DHUNINV.NS', 
'DIAMONDYD.NS', 
'DIAPOWER.NS', 
'DICIND.NS', 
'DIGISPICE.NS', 
'DIGJAMLMTD.NS', 
'DIL.NS', 
'DISHTV.NS', 
'DIVISLAB.NS', 
'DIXON.NS', 
'DJML.NS', 
'DKEGL.NS', 
'DLF.NS', 
'DLINKINDIA.NS', 
'DMART.NS', 
'DMCC.NS', 
'DNAMEDIA.NS', 
'DODLA.NS', 
'DOLLAR.NS', 
'DOLLEX.NS', 
'DOLPHINOFF.NS', 
'DONEAR.NS', 
'DPABHUSHAN.NS', 
'DPSCLTD.NS', 
'DPWIRES.NS', 
'DQE.NS', 
'DRCSYSTEMS.NS', 
'DREAMFOLKS.NS', 
'DREDGECORP.NS', 
'DRL.NS', 
'DRREDDY.NS', 
'DRSDILIP.NS', 
'DSKULKARNI.NS', 
'DSSL.NS', 
'DTIL.NS', 
'DUCON.NS', 
'DUGLOBAL.NS', 
'DVL.NS', 
'DWARKESH.NS', 
'DYCL.NS', 
'DYNAMATECH.NS', 
'DYNAMIC.NS', 
'DYNPRO.NS', 
'E2E.NS', 
'EASEMYTRIP.NS', 
'EASTSILK.NS', 
'EASTSUGIND.NS', 
'EASUNREYRL.NS', 
'ECLERX.NS', 
'EDELWEISS.NS', 
'EDUCOMP.NS', 
'EICHERMOT.NS', 
'EIDPARRY.NS', 
'EIFFL.NS', 
'EIHAHOTELS.NS', 
'EIHOTEL.NS', 
'EIMCOELECO.NS', 
'EKC.NS', 
'ELDEHSG.NS', 
'ELECON.NS', 
'ELECTCAST.NS', 
'ELECTHERM.NS', 
'ELGIEQUIP.NS', 
'ELGIRUBCO.NS', 
'ELIN.NS', 
'EMAMILTD.NS', 
'EMAMIPAP.NS', 
'EMAMIREAL.NS', 
'EMCO.NS', 
'EMIL.NS', 
'EMKAY.NS', 
'EMKAYTOOLS.NS', 
'EMMBI.NS', 
'EMUDHRA.NS', 
'ENDURANCE.NS', 
'ENERGYDEV.NS', 
'ENGINERSIN.NS', 
'ENIL.NS', 
'EON.NS', 
'EPL.NS', 
'EQUIPPP.NS', 
'EQUITAS.NS', 
'EQUITASBNK.NS', 
'ERIS.NS', 
'EROSMEDIA.NS', 
'ESABINDIA.NS', 
'ESCORTS.NS', 
'ESSARSHPNG.NS', 
'ESSENTIA.NS', 
'ESTER.NS', 
'ETHOSLTD.NS', 
'EUROBOND.NS', 
'EUROCERA.NS', 
'EUROMULTI.NS', 
'EUROTEXIND.NS', 
'EVEREADY.NS', 
'EVERESTIND.NS', 
'EXCEL.NS', 
'EXCELINDUS.NS', 
'EXIDEIND.NS', 
'EXPLEOSOL.NS', 
'EXXARO.NS', 
'FACT.NS', 
'FAIRCHEMOR.NS', 
'FAZE3Q.NS', 
'FCL.NS', 
'FCONSUMER.NS', 
'FCSSOFT.NS', 
'FDC.NS', 
'FEDDERELEC.NS', 
'FEDERALBNK.NS', 
'FEL.NS', 
'FELIX.NS', 
'FIBERWEB.NS', 
'FIDEL.NS', 
'FIEMIND.NS', 
'FILATEX.NS', 
'FINCABLES.NS', 
'FINEORG.NS', 
'FINOPB.NS', 
'FINPIPE.NS', 
'FIVECORE.NS', 
'FIVESTAR.NS', 
'FLEXITUFF.NS', 
'FLFL.NS', 
'FLUOROCHEM.NS', 
'FMGOETZE.NS', 
'FMNL.NS', 
'FOCE.NS', 
'FOCUS.NS', 
'FOODSIN.NS', 
'FORTIS.NS', 
'FOSECOIND.NS', 
'FRETAIL.NS', 
'FROG.NS', 
'FSC.NS', 
'FSL.NS', 
'FUSION.NS', 
'GABRIEL.NS', 
'GAEL.NS', 
'GAIL.NS', 
'GAL.NS', 
'GALAXYSURF.NS', 
'GALLANTT.NS', 
'GAMMONIND.NS', 
'GANDHITUBE.NS', 
'GANECOS.NS', 
'GANESHBE.NS', 
'GANESHHOUC.NS', 
'GANGAFORGE.NS', 
'GANGESSECU.NS', 
'GANGOTRI.NS', 
'GARFIBRES.NS', 
'GATEWAY.NS', 
'GATI.NS', 
'GAYAHWS.NS', 
'GAYAPROJ.NS', 
'GBGLOBAL.NS', 
'GEECEE.NS', 
'GEEKAYWIRE.NS', 
'GENCON.NS', 
'GENESYS.NS', 
'GENUSPAPER.NS', 
'GENUSPOWER.NS', 
'GEOJITFSL.NS', 
'GEPIL.NS', 
'GESHIP.NS', 
'GET&D.NS', 
'GFLLIMITED.NS', 
'GFSTEELS.NS', 
'GHCL.NS', 
'GICHSGFIN.NS', 
'GICL.NS', 
'GICRE.NS', 
'GILLANDERS.NS', 
'GILLETTE.NS', 
'GINNIFILA.NS', 
'GIPCL.NS', 
'GIRIRAJ.NS', 
'GIRRESORTS.NS', 
'GISOLUTION.NS', 
'GITANJALI.NS', 
'GKWLIMITED.NS', 
'GLAND.NS', 
'GLAXO.NS', 
'GLENMARK.NS', 
'GLFL.NS', 
'GLOBAL.NS', 
'GLOBALVECT.NS', 
'GLOBE.NS', 
'GLOBUSSPR.NS', 
'GLS.NS', 
'GMBREW.NS', 
'GMDCLTD.NS', 
'GMMPFAUDLR.NS', 
'GMRINFRA.NS', 
'GMRP&UI.NS', 
'GNA.NS', 
'GNFC.NS', 
'GOACARBON.NS', 
'GOCLCORP.NS', 
'GOCOLORS.NS', 
'GODFRYPHLP.NS', 
'GODHA.NS', 
'GODREJAGRO.NS', 
'GODREJCP.NS', 
'GODREJIND.NS', 
'GODREJPROP.NS', 
'GOENKA.NS', 
'GOKEX.NS', 
'GOKUL.NS', 
'GOKULAGRO.NS', 
'GOLDENTOBC.NS', 
'GOLDIAM.NS', 
'GOLDSTAR.NS', 
'GOLDTECH.NS', 
'GOODLUCK.NS', 
'GOYALALUM.NS', 
'GPIL.NS', 
'GPPL.NS', 
'GPTINFRA.NS', 
'GRANULES.NS', 
'GRAPHITE.NS', 
'GRASIM.NS', 
'GRAVITA.NS', 
'GREAVESCOT.NS', 
'GREENLAM.NS', 
'GREENPANEL.NS', 
'GREENPLY.NS', 
'GREENPOWER.NS', 
'GRETEX.NS', 
'GRINDWELL.NS', 
'GRINFRA.NS', 
'GRMOVER.NS', 
'GROBTEA.NS', 
'GRPLTD.NS', 
'GRSE.NS', 
'GRWRHITECH.NS', 
'GSCLCEMENT.NS', 
'GSFC.NS', 
'GSPL.NS', 
'GSS.NS', 
'GSTL.NS', 
'GTL.NS', 
'GTLINFRA.NS', 
'GTPL.NS', 
'GUFICBIO.NS', 
'GUJALKALI.NS', 
'GUJAPOLLO.NS', 
'GUJGASLTD.NS', 
'GUJRAFFIA.NS', 
'GULFOILLUB.NS', 
'GULFPETRO.NS', 
'GULPOLY.NS', 
'GVKPIL.NS', 
'HAL.NS', 
'HAPPSTMNDS.NS', 
'HARDWYN.NS', 
'HARIOMPIPE.NS', 
'HARRMALAYA.NS', 
'HARSHA.NS', 
'HATHWAY.NS', 
'HATSUN.NS', 
'HAVELLS.NS', 
'HAVISHA.NS', 
'HBLPOWER.NS', 
'HBSL.NS', 
'HCC.NS', 
'HCG.NS', 
'HCL-INSYS.NS', 
'HCLTECH.NS', 
'HDFC.NS', 
'HDFCAMC.NS', 
'HDFCBANK.NS', 
'HDFCLIFE.NS', 
'HDIL.NS', 
'HEADSUP.NS', 
'HECPROJECT.NS', 
'HEG.NS', 
'HEIDELBERG.NS', 
'HEMIPROP.NS', 
'HERANBA.NS', 
'HERCULES.NS', 
'HERITGFOOD.NS', 
'HEROMOTOCO.NS', 
'HESTERBIO.NS', 
'HEXATRADEX.NS', 
'HFCL.NS', 
'HGINFRA.NS', 
'HGS.NS', 
'HIKAL.NS', 
'HIL.NS', 
'HILTON.NS', 
'HIMATSEIDE.NS', 
'HINDALCO.NS', 
'HINDCOMPOS.NS', 
'HINDCON.NS', 
'HINDCOPPER.NS', 
'HINDMOTORS.NS', 
'HINDNATGLS.NS', 
'HINDOILEXP.NS', 
'HINDPETRO.NS', 
'HINDUNILVR.NS', 
'HINDWAREAP.NS', 
'HINDZINC.NS', 
'HIRECT.NS', 
'HISARMETAL.NS', 
'HITECH.NS', 
'HITECHCORP.NS', 
'HITECHGEAR.NS', 
'HLVLTD.NS', 
'HMT.NS', 
'HMVL.NS', 
'HOMEFIRST.NS', 
'HONAUT.NS', 
'HONDAPOWER.NS', 
'HOVS.NS', 
'HPAL.NS', 
'HPIL.NS', 
'HPL.NS', 
'HSCL.NS', 
'HTMEDIA.NS', 
'HUBTOWN.NS', 
'HUDCO.NS', 
'HUHTAMAKI.NS', 
'HYBRIDFIN.NS', 
'IBREALEST.NS', 
'IBULHSGFIN.NS', 
'ICDSLTD.NS', 
'ICEMAKE.NS', 
'ICICIBANK.NS', 
'ICICIGI.NS', 
'ICICIPRULI.NS', 
'ICIL.NS', 
'ICRA.NS', 
'ICSA.NS', 
'IDBI.NS', 
'IDEA.NS', 
'IDFC.NS', 
'IDFCFIRSTB.NS', 
'IEL.NS', 
'IEX.NS', 
'IFBAGRO.NS', 
'IFBIND.NS', 
'IFCI.NS', 
'IFGLEXPOR.NS', 
'IGARASHI.NS', 
'IGL.NS', 
'IGPL.NS', 
'IIFL.NS', 
'IIFLSEC.NS', 
'IIFLWAM.NS', 
'IITL.NS', 
'IL&FSENGG.NS', 
'IL&FSTRANS.NS', 
'IMAGICAA.NS', 
'IMFA.NS', 
'IMPAL.NS', 
'IMPEXFERRO.NS', 
'INCREDIBLE.NS', 
'INDBANK.NS', 
'INDHOTEL.NS', 
'INDIACEM.NS', 
'INDIAGLYCO.NS', 
'INDIAMART.NS', 
'INDIANB.NS', 
'INDIANCARD.NS', 
'INDIANHUME.NS', 
'INDIGO.NS', 
'INDIGOPNTS.NS', 
'INDLMETER.NS', 
'INDNIPPON.NS', 
'INDOAMIN.NS', 
'INDOBORAX.NS', 
'INDOCO.NS', 
'INDORAMA.NS', 
'INDOSOLAR.NS', 
'INDOSTAR.NS', 
'INDOTECH.NS', 
'INDOTHAI.NS', 
'INDOWIND.NS', 
'INDRAMEDCO.NS', 
'INDSWFTLAB.NS', 
'INDSWFTLTD.NS', 
'INDTERRAIN.NS', 
'INDUSINDBK.NS', 
'INDUSTOWER.NS', 
'INEOSSTYRO.NS', 
'INFIBEAM.NS', 
'INFOBEAN.NS', 
'INFOMEDIA.NS', 
'INFY.NS', 
'INGERRAND.NS', 
'INNOVANA.NS', 
'INNOVATIVE.NS', 
'INOXGREEN.NS', 
'INOXLEISUR.NS', 
'INOXWIND.NS', 
'INSECTICID.NS', 
'INSPIRISYS.NS', 
'INTELLECT.NS', 
'INTENTECH.NS', 
'INTLCONV.NS', 
'INVENTURE.NS', 
'IOB.NS', 
'IOC.NS', 
'IOLCP.NS', 
'IONEXCHANG.NS', 
'IPCALAB.NS', 
'IPL.NS', 
'IPSL.NS', 
'IRB.NS', 
'IRCON.NS', 
'IRCTC.NS', 
'IRFC.NS', 
'IRIS.NS', 
'IRISDOREME.NS', 
'ISEC.NS', 
'ISFT.NS', 
'ISGEC.NS', 
'ISHAN.NS', 
'ISMTLTD.NS', 
'ITC.NS', 
'ITDC.NS', 
'ITDCEM.NS', 
'ITI.NS', 
'IVC.NS', 
'IVP.NS', 
'IVRCLINFRA.NS', 
'IWEL.NS', 
'IZMO.NS', 
'J&KBANK.NS', 
'JAGRAN.NS', 
'JAGSNPHARM.NS', 
'JAIBALAJI.NS', 
'JAICORPLTD.NS', 
'JAINAM.NS', 
'JAINSTUDIO.NS', 
'JAIPURKURT.NS', 
'JAKHARIA.NS', 
'JALAN.NS', 
'JAMNAAUTO.NS', 
'JASH.NS', 
'JAYAGROGN.NS', 
'JAYBARMARU.NS', 
'JAYNECOIND.NS', 
'JAYSREETEA.NS', 
'JBCHEPHARM.NS', 
'JBFIND.NS', 
'JBMA.NS', 
'JCHAC.NS', 
'JETAIRWAYS.NS', 
'JETFREIGHT.NS', 
'JETKNIT.NS', 
'JFLLIFE.NS', 
'JHS.NS', 
'JIKIND.NS', 
'JINDALPHOT.NS', 
'JINDALPOLY.NS', 
'JINDALSAW.NS', 
'JINDALSTEL.NS', 
'JINDCOT.NS', 
'JINDRILL.NS', 
'JINDWORLD.NS', 
'JISLJALEQS.NS', 
'JITFINFRA.NS', 
'JKCEMENT.NS', 
'JKIL.NS', 
'JKLAKSHMI.NS', 
'JKPAPER.NS', 
'JKTYRE.NS', 
'JMA.NS', 
'JMCPROJECT.NS', 
'JMFINANCIL.NS', 
'JMTAUTOLTD.NS', 
'JOCIL.NS', 
'JPASSOCIAT.NS', 
'JPINFRATEC.NS', 
'JPOLYINVST.NS', 
'JPPOWER.NS', 
'JSL.NS', 
'JSLHISAR.NS', 
'JSLL.NS', 
'JSWENERGY.NS', 
'JSWHL.NS', 
'JSWISPL.NS', 
'JSWSTEEL.NS', 
'JTEKTINDIA.NS', 
'JUBLFOOD.NS', 
'JUBLINDS.NS', 
'JUBLINGREA.NS', 
'JUBLPHARMA.NS', 
'JUSTDIAL.NS', 
'JWL.NS', 
'JYOTHYLAB.NS', 
'JYOTISTRUC.NS', 
'KABRAEXTRU.NS', 
'KAJARIACER.NS', 
'KAKATCEM.NS', 
'KALPATPOWR.NS', 
'KALYANI.NS', 
'KALYANIFRG.NS', 
'KALYANKJIL.NS', 
'KAMATHOTEL.NS', 
'KAMDHENU.NS', 
'KANANIIND.NS', 
'KANDARP.NS', 
'KANORICHEM.NS', 
'KANPRPLA.NS', 
'KANSAINER.NS', 
'KAPSTON.NS', 
'KARMAENG.NS', 
'KARURVYSYA.NS', 
'KAUSHALYA.NS', 
'KAVVERITEL.NS', 
'KAYA.NS', 
'KAYNES.NS', 
'KBCGLOBAL.NS', 
'KCK.NS', 
'KCP.NS', 
'KCPSUGIND.NS', 
'KDDL.NS', 
'KEC.NS', 
'KECL.NS', 
'KEEPLEARN.NS', 
'KEERTI.NS', 
'KEI.NS', 
'KELLTONTEC.NS', 
'KERNEX.NS', 
'KESORAMIND.NS', 
'KEYFINSERV.NS', 
'KFINTECH.NS', 
'KGL.NS', 
'KHADIM.NS', 
'KHAICHEM.NS', 
'KHAITANLTD.NS', 
'KHANDSE.NS', 
'KHFM.NS', 
'KICL.NS', 
'KILITCH.NS', 
'KIMS.NS', 
'KINGFA.NS', 
'KIOCL.NS', 
'KIRIINDUS.NS', 
'KIRLOSBROS.NS', 
'KIRLOSENG.NS', 
'KIRLOSIND.NS', 
'KITEX.NS', 
'KKCL.NS', 
'KKVAPOW.NS', 
'KMSUGAR.NS', 
'KNAGRI.NS', 
'KNRCON.NS', 
'KOHINOOR.NS', 
'KOKUYOCMLN.NS', 
'KOLTEPATIL.NS', 
'KOPRAN.NS', 
'KORE.NS', 
'KOTAKBANK.NS', 
'KOTARISUG.NS', 
'KOTHARIPET.NS', 
'KOTHARIPRO.NS', 
'KOTYARK.NS', 
'KPIGREEN.NS', 
'KPITTECH.NS', 
'KPRMILL.NS', 
'KRBL.NS', 
'KREBSBIO.NS', 
'KRIDHANINF.NS', 
'KRISHANA.NS', 
'KRISHIVAL.NS', 
'KRISHNADEF.NS', 
'KRITI.NS', 
'KRITIKA.NS', 
'KRITINUT.NS', 
'KRSNAA.NS', 
'KSB.NS', 
'KSCL.NS', 
'KSERASERA.NS', 
'KSHITIJPOL.NS', 
'KSK.NS', 
'KSL.NS', 
'KSOLVES.NS', 
'KTKBANK.NS', 
'KUANTUM.NS', 
'L&TFH.NS', 
'LAGNAM.NS', 
'LAKPRE.NS', 
'LAKSHMIEFL.NS', 
'LALPATHLAB.NS', 
'LAMBODHARA.NS', 
'LANDMARK.NS', 
'LAOPALA.NS', 
'LASA.NS', 
'LATENTVIEW.NS', 
'LATTEYS.NS', 
'LAURUSLABS.NS', 
'LAXMICOT.NS', 
'LAXMIMACH.NS', 
'LCCINFOTEC.NS', 
'LEEL.NS', 
'LEMERITE.NS', 
'LEMONTREE.NS', 
'LEXUS.NS', 
'LFIC.NS', 
'LGBBROSLTD.NS', 
'LGBFORGE.NS', 
'LGHL.NS', 
'LIBAS.NS', 
'LIBERTSHOE.NS', 
'LICHSGFIN.NS', 
'LICI.NS', 
'LIKHITHA.NS', 
'LINC.NS', 
'LINCOLN.NS', 
'LINDEINDIA.NS', 
'LLOYDS.NS', 
'LODHA.NS', 
'LOKESHMACH.NS', 
'LOTUSEYE.NS', 
'LOVABLE.NS', 
'LOYALTEX.NS', 
'LPDC.NS', 
'LSIL.NS', 
'LT.NS', 
'LTIM.NS', 
'LTTS.NS', 
'LUMAXIND.NS', 
'LUMAXTECH.NS', 
'LUPIN.NS', 
'LUXIND.NS', 
'LXCHEM.NS', 
'LYKALABS.NS', 
'LYPSAGEMS.NS', 
'M&M.NS', 
'M&MFIN.NS', 
'MAANALU.NS', 
'MACPOWER.NS', 
'MADHAV.NS', 
'MADHAVBAUG.NS', 
'MADHUCON.NS', 
'MADRASFERT.NS', 
'MAGADSUGAR.NS', 
'MAGNUM.NS', 
'MAHABANK.NS', 
'MAHAPEXLTD.NS', 
'MAHASTEEL.NS', 
'MAHEPC.NS', 
'MAHESHWARI.NS', 
'MAHICKRA.NS', 
'MAHINDCIE.NS', 
'MAHLIFE.NS', 
'MAHLOG.NS', 
'MAHSCOOTER.NS', 
'MAHSEAMLES.NS', 
'MAITHANALL.NS', 
'MAKS.NS', 
'MALLCOM.NS', 
'MALUPAPER.NS', 
'MANAKALUCO.NS', 
'MANAKCOAT.NS', 
'MANAKSIA.NS', 
'MANAKSTEEL.NS', 
'MANALIPETC.NS', 
'MANAPPURAM.NS', 
'MANAV.NS', 
'MANGALAM.NS', 
'MANGCHEFER.NS', 
'MANGLMCEM.NS', 
'MANINDS.NS', 
'MANINFRA.NS', 
'MANORAMA.NS', 
'MANORG.NS', 
'MANPASAND.NS', 
'MANUGRAPH.NS', 
'MANYAVAR.NS', 
'MAPMYINDIA.NS', 
'MARALOVER.NS', 
'MARATHON.NS', 
'MARICO.NS', 
'MARINE.NS', 
'MARKSANS.NS', 
'MARSHALL.NS', 
'MARUTI.NS', 
'MASFIN.NS', 
'MASKINVEST.NS', 
'MASTEK.NS', 
'MATRIMONY.NS', 
'MAWANASUG.NS', 
'MAXHEALTH.NS', 
'MAXIND.NS', 
'MAXVIL.NS', 
'MAYURUNIQ.NS', 
'MAZDA.NS', 
'MAZDOCK.NS', 
'MBAPL.NS', 
'MBECL.NS', 
'MBLINFRA.NS', 
'MCDHOLDING.NS', 
'MCDOWELL-N.NS', 
'MCL.NS', 
'MCLEODRUSS.NS', 
'MDL.NS', 
'MEDANTA.NS', 
'MEDICAMEQ.NS', 
'MEDICO.NS', 
'MEDPLUS.NS', 
'MEGAFLEX.NS', 
'MEGASOFT.NS', 
'MEGASTAR.NS', 
'MELSTAR.NS', 
'MENONBE.NS', 
'MEP.NS', 
'MERCATOR.NS', 
'METALFORGE.NS', 
'METKORE.NS', 
'METROBRAND.NS', 
'METROPOLIS.NS', 
'MFL.NS', 
'MFSL.NS', 
'MGEL.NS', 
'MGL.NS', 
'MHHL.NS', 
'MHLXMIRU.NS', 
'MHRIL.NS', 
'MICEL.NS', 
'MIDHANI.NS', 
'MILTON.NS', 
'MINDACORP.NS', 
'MINDPOOL.NS', 
'MINDTECK.NS', 
'MIRCELECTR.NS', 
'MIRZAINT.NS', 
'MITCON.NS', 
'MITTAL.NS', 
'MKPL.NS', 
'MMFL.NS', 
'MMP.NS', 
'MMTC.NS', 
'MODIRUBBER.NS', 
'MODISONLTD.NS', 
'MODTHREAD.NS', 
'MOHITIND.NS', 
'MOHOTAIND.NS', 
'MOIL.NS', 
'MOKSH.NS', 
'MOL.NS', 
'MOLDTECH.NS', 
'MOLDTKPAC.NS', 
'MONARCH.NS', 
'MONTECARLO.NS', 
'MORARJEE.NS', 
'MOREPENLAB.NS', 
'MOTHERSON.NS', 
'MOTILALOFS.NS', 
'MOTOGENFIN.NS', 
'MOXSH.NS', 
'MPHASIS.NS', 
'MPSLTD.NS', 
'MPTODAY.NS', 
'MRF.NS', 
'MRO-TEK.NS', 
'MRO.NS', 
'MRPL.NS', 
'MSPL.NS', 
'MSTCLTD.NS', 
'MSUMI.NS', 
'MTARTECH.NS', 
'MTEDUCARE.NS', 
'MTNL.NS', 
'MUKANDLTD.NS', 
'MUKTAARTS.NS', 
'MUNJALAU.NS', 
'MUNJALSHOW.NS', 
'MURUDCERA.NS', 
'MUTHOOTCAP.NS', 
'MUTHOOTFIN.NS', 
'MVL.NS', 
'MWL.NS', 
'NACLIND.NS', 
'NAGAFERT.NS', 
'NAGREEKCAP.NS', 
'NAGREEKEXP.NS', 
'NAHARCAP.NS', 
'NAHARINDUS.NS', 
'NAHARPOLY.NS', 
'NAHARSPING.NS', 
'NAKODA.NS', 
'NAM-INDIA.NS', 
'NARMADA.NS', 
'NATCOPHARM.NS', 
'NATHBIOGEN.NS', 
'NATIONALUM.NS', 
'NATNLSTEEL.NS', 
'NAUKRI.NS', 
'NAVA.NS', 
'NAVINFLUOR.NS', 
'NAVKARCORP.NS', 
'NAVNETEDUL.NS', 
'NAZARA.NS', 
'NBCC.NS', 
'NBIFIN.NS', 
'NCC.NS', 
'NCLIND.NS', 
'NDGL.NS', 
'NDL.NS', 
'NDRAUTO.NS', 
'NDTV.NS', 
'NECCLTD.NS', 
'NECLIFE.NS', 
'NELCAST.NS', 
'NELCO.NS', 
'NEOGEN.NS', 
'NESCO.NS', 
'NETWORK18.NS', 
'NEULANDLAB.NS', 
'NEWGEN.NS', 
'NEXTMEDIA.NS', 
'NFL.NS', 
'NGIL.NS', 
'NGLFINE.NS', 
'NH.NS', 
'NHPC.NS', 
'NIACL.NS', 
'NIBL.NS', 
'NIDAN.NS', 
'NIITLTD.NS', 
'NILAINFRA.NS', 
'NILASPACES.NS', 
'NILKAMAL.NS', 
'NIPPOBATRY.NS', 
'NIRAJ.NS', 
'NIRAJISPAT.NS', 
'NITCO.NS', 
'NITINFIRE.NS', 
'NITINSPIN.NS', 
'NITIRAJ.NS', 
'NKIND.NS', 
'NLCINDIA.NS', 
'NMDC.NS', 
'NOCIL.NS', 
'NOIDATOLL.NS', 
'NORBTEAEXP.NS', 
'NPST.NS', 
'NRAIL.NS', 
'NRBBEARING.NS', 
'NRL.NS', 
'NSIL.NS', 
'NTL.NS', 
'NTPC.NS', 
'NUCLEUS.NS', 
'NURECA.NS', 
'NUTEK.NS', 
'NUVOCO.NS', 
'NXTDIGITAL.NS', 
'NYKAA.NS', 
'OAL.NS', 
'OBCL.NS', 
'OBEROIRLTY.NS', 
'OCCL.NS', 
'OFSS.NS', 
'OIL.NS', 
'OILCOUNTUB.NS', 
'OISL.NS', 
'OLECTRA.NS', 
'OMAXAUTO.NS', 
'OMAXE.NS', 
'OMFURN.NS', 
'OMINFRAL.NS', 
'OMKARCHEM.NS', 
'ONELIFECAP.NS', 
'ONEPOINT.NS', 
'ONGC.NS', 
'ONMOBILE.NS', 
'ONWARDTEC.NS', 
'OPAL.NS', 
'OPTIEMUS.NS', 
'OPTOCIRCUI.NS', 
'ORBTEXP.NS', 
'ORCHPHARMA.NS', 
'ORICONENT.NS', 
'ORIENTABRA.NS', 
'ORIENTALTL.NS', 
'ORIENTBELL.NS', 
'ORIENTCEM.NS', 
'ORIENTELEC.NS', 
'ORIENTHOT.NS', 
'ORIENTLTD.NS', 
'ORIENTPPR.NS', 
'ORISSAMINE.NS', 
'ORTEL.NS', 
'ORTINLAB.NS', 
'OSIAHYPER.NS', 
'OSWALAGRO.NS', 
'OSWALSEEDS.NS', 
'PAGEIND.NS', 
'PAISALO.NS', 
'PALASHSECU.NS', 
'PALREDTEC.NS', 
'PANACEABIO.NS', 
'PANACHE.NS', 
'PANAMAPET.NS', 
'PANSARI.NS', 
'PAR.NS', 
'PARACABLES.NS', 
'PARADEEP.NS', 
'PARAGMILK.NS', 
'PARAS.NS', 
'PARASPETRO.NS', 
'PARIN.NS', 
'PARSVNATH.NS', 
'PARTYCRUS.NS', 
'PASHUPATI.NS', 
'PASUPTAC.NS', 
'PATANJALI.NS', 
'PATELENG.NS', 
'PATINTLOG.NS', 
'PAVNAIND.NS', 
'PAYTM.NS', 
'PCBL.NS', 
'PCJEWELLER.NS', 
'PDMJEPAPER.NS', 
'PDPL.NS', 
'PDSL.NS', 
'PEARLPOLY.NS', 
'PEL.NS', 
'PENIND.NS', 
'PENINLAND.NS', 
'PENTAGOLD.NS', 
'PERFECT.NS', 
'PERSISTENT.NS', 
'PETRONET.NS', 
'PFC.NS', 
'PFIZER.NS', 
'PFOCUS.NS', 
'PFS.NS', 
'PGEL.NS', 
'PGHH.NS', 
'PGHL.NS', 
'PGIL.NS', 
'PHANTOMFX.NS', 
'PHOENIXLTD.NS', 
'PIDILITIND.NS', 
'PIGL.NS', 
'PIIND.NS', 
'PILANIINVS.NS', 
'PILITA.NS', 
'PINCON.NS', 
'PIONDIST.NS', 
'PIONEEREMB.NS', 
'PITTIENG.NS', 
'PIXTRANS.NS', 
'PKTEA.NS', 
'PLASTIBLEN.NS', 
'PNB.NS', 
'PNBGILTS.NS', 
'PNBHOUSING.NS', 
'PNC.NS', 
'PNCINFRA.NS', 
'PODDARHOUS.NS', 
'PODDARMENT.NS', 
'POKARNA.NS', 
'POLICYBZR.NS', 
'POLYCAB.NS', 
'POLYMED.NS', 
'POLYPLEX.NS', 
'PONNIERODE.NS', 
'POONAWALLA.NS', 
'POWERFUL.NS', 
'POWERGRID.NS', 
'POWERINDIA.NS', 
'POWERMECH.NS', 
'PPAP.NS', 
'PPL.NS', 
'PPLPHARMA.NS', 
'PRAENG.NS', 
'PRAJIND.NS', 
'PRAKASH.NS', 
'PRAKASHSTL.NS', 
'PRATIBHA.NS', 
'PRAXIS.NS', 
'PRECAM.NS', 
'PRECISION.NS', 
'PRECOT.NS', 
'PRECWIRE.NS', 
'PREMEXPLN.NS', 
'PREMIER.NS', 
'PREMIERPOL.NS', 
'PRESSMN.NS', 
'PRESTIGE.NS', 
'PRICOLLTD.NS', 
'PRIMESECU.NS', 
'PRINCEPIPE.NS', 
'PRITI.NS', 
'PRITIKA.NS', 
'PRITIKAUTO.NS', 
'PRIVISCL.NS', 
'PROLIFE.NS', 
'PROPEQUITY.NS', 
'PROZONINTU.NS', 
'PRSMJOHNSN.NS', 
'PRUDENT.NS', 
'PRUDMOULI.NS', 
'PSB.NS', 
'PSL.NS', 
'PSPPROJECT.NS', 
'PTC.NS', 
'PTL.NS', 
'PULZ.NS', 
'PUNJABCHEM.NS', 
'PUNJLLOYD.NS', 
'PURVA.NS', 
'PVP.NS', 
'PVR.NS', 
'QMSMEDI.NS', 
'QUADPRO.NS', 
'QUESS.NS', 
'QUICKHEAL.NS', 
'QUINTEGRA.NS', 
'RADAAN.NS', 
'RADHIKAJWE.NS', 
'RADICO.NS', 
'RADIOCITY.NS', 
'RAILTEL.NS', 
'RAIN.NS', 
'RAINBOW.NS', 
'RAINBOWPAP.NS', 
'RAJESHEXPO.NS', 
'RAJMET.NS', 
'RAJRATAN.NS', 
'RAJRILTD.NS', 
'RAJSREESUG.NS', 
'RAJTV.NS', 
'RAJVIR.NS', 
'RALLIS.NS', 
'RAMANEWS.NS', 
'RAMAPHO.NS', 
'RAMASTEEL.NS', 
'RAMCOCEM.NS', 
'RAMCOIND.NS', 
'RAMCOSYS.NS', 
'RAMKY.NS', 
'RAMRAT.NS', 
'RANASUG.NS', 
'RANEENGINE.NS', 
'RANEHOLDIN.NS', 
'RATEGAIN.NS', 
'RATNAMANI.NS', 
'RAYMOND.NS', 
'RBA.NS', 
'RBL.NS', 
'RBLBANK.NS', 
'RCF.NS', 
'RCOM.NS', 
'RECLTD.NS', 
'REDINGTON.NS', 
'REFEX.NS', 
'REGENCERAM.NS', 
'RELAXO.NS', 
'RELCAPITAL.NS', 
'RELCHEMQ.NS', 
'RELIABLE.NS', 
'RELIANCE.NS', 
'RELIGARE.NS', 
'RELINFRA.NS', 
'REMSONSIND.NS', 
'RENUKA.NS', 
'REPCOHOME.NS', 
'REPL.NS', 
'REPRO.NS', 
'RESPONIND.NS', 
'REVATHI.NS', 
'REXPIPES.NS', 
'RGL.NS', 
'RHFL.NS', 
'RHIM.NS', 
'RICHA.NS', 
'RICOAUTO.NS', 
'RIIL.NS', 
'RILINFRA.NS', 
'RITCO.NS', 
'RITES.NS', 
'RITEZONE.NS', 
'RKDL.NS', 
'RKEC.NS', 
'RKFORGE.NS', 
'RMCL.NS', 
'RMDRIP.NS', 
'RML.NS', 
'RMMIL.NS', 
'RNAVAL.NS', 
'ROHLTD.NS', 
'ROLEXRINGS.NS', 
'ROLLT.NS', 
'ROLTA.NS', 
'ROML.NS', 
'ROSSARI.NS', 
'ROSSELLIND.NS', 
'ROTO.NS', 
'ROUTE.NS', 
'RPGLIFE.NS', 
'RPOWER.NS', 
'RPPINFRA.NS', 
'RPPL.NS', 
'RPSGVENT.NS', 
'RSSOFTWARE.NS', 
'RSWM.NS', 
'RSYSTEMS.NS', 
'RTNINDIA.NS', 
'RTNPOWER.NS', 
'RUBYMILLS.NS', 
'RUCHINFRA.NS', 
'RUCHIRA.NS', 
'RUPA.NS', 
'RUSHABEAR.NS', 
'RUSHIL.NS', 
'RUSTOMJEE.NS', 
'RVHL.NS', 
'RVNL.NS', 
'S&SPOWER.NS', 
'SABAR.NS', 
'SABEVENTS.NS', 
'SABTN.NS', 
'SADBHAV.NS', 
'SADBHIN.NS', 
'SAFARI.NS', 
'SAGARDEEP.NS', 
'SAGCEM.NS', 
'SAIL.NS', 
'SAKAR.NS', 
'SAKHTISUG.NS', 
'SAKSOFT.NS', 
'SAKUMA.NS', 
'SALASAR.NS', 
'SALONA.NS', 
'SALSTEEL.NS', 
'SALZERELEC.NS', 
'SAMBHAAV.NS', 
'SANCO.NS', 
'SANDESH.NS', 
'SANDHAR.NS', 
'SANGAMIND.NS', 
'SANGHIIND.NS', 
'SANGHVIMOV.NS', 
'SANGINITA.NS', 
'SANOFI.NS', 
'SANSERA.NS', 
'SANWARIA.NS', 
'SAPPHIRE.NS', 
'SARDAEN.NS', 
'SAREGAMA.NS', 
'SARLAPOLY.NS', 
'SARVESHWAR.NS', 
'SASKEN.NS', 
'SASTASUNDR.NS', 
'SATHAISPAT.NS', 
'SATIA.NS', 
'SATIN.NS', 
'SATINDLTD.NS', 
'SBC.NS', 
'SBCL.NS', 
'SBICARD.NS', 
'SBIHOMEFIN.NS', 
'SBILIFE.NS', 
'SBIN.NS', 
'SCHAEFFLER.NS', 
'SCHAND.NS', 
'SCHNEIDER.NS', 
'SCI.NS', 
'SCPL.NS', 
'SDBL.NS', 
'SEAMECLTD.NS', 
'SECL.NS', 
'SECURCRED.NS', 
'SECURKLOUD.NS', 
'SEJALLTD.NS', 
'SELAN.NS', 
'SELMC.NS', 
'SEPC.NS', 
'SEPOWER.NS', 
'SEQUENT.NS', 
'SERVOTECH.NS', 
'SESHAPAPER.NS', 
'SETCO.NS', 
'SETUINFRA.NS', 
'SEYAIND.NS', 
'SFL.NS', 
'SGIL.NS', 
'SGL.NS', 
'SHAHALLOYS.NS', 
'SHAILY.NS', 
'SHAIVAL.NS', 
'SHAKTIPUMP.NS', 
'SHALBY.NS', 
'SHALPAINTS.NS', 
'SHANKARA.NS', 
'SHANTI.NS', 
'SHANTIGEAR.NS', 
'SHARDACROP.NS', 
'SHARDAMOTR.NS', 
'SHAREINDIA.NS', 
'SHARONBIO.NS', 
'SHEMAROO.NS', 
'SHIGAN.NS', 
'SHILPAMED.NS', 
'SHIRPUR-G.NS', 
'SHIVALIK.NS', 
'SHIVAMAUTO.NS', 
'SHIVAMILLS.NS', 
'SHIVATEX.NS', 
'SHIVAUM.NS', 
'SHK.NS', 
'SHOPERSTOP.NS', 
'SHRADHA.NS', 
'SHREDIGCEM.NS', 
'SHREECEM.NS', 
'SHREEPUSHK.NS', 
'SHREERAMA.NS', 
'SHRENIK.NS', 
'SHREYANIND.NS', 
'SHREYAS.NS', 
'SHRIPISTON.NS', 
'SHRIRAMFIN.NS', 
'SHRIRAMPPS.NS', 
'SHUBHLAXMI.NS', 
'SHYAMCENT.NS', 
'SHYAMMETL.NS', 
'SHYAMTEL.NS', 
'SICAL.NS', 
'SIDDHIKA.NS', 
'SIEMENS.NS', 
'SIGACHI.NS', 
'SIGIND.NS', 
'SIGMA.NS', 
'SIIL.NS', 
'SIKKO.NS', 
'SIL.NS', 
'SILGO.NS', 
'SILINV.NS', 
'SILLYMONKS.NS', 
'SILVERTUC.NS', 
'SIMBHALS.NS', 
'SIMPLEXINF.NS', 
'SINTERCOM.NS', 
'SINTEX.NS', 
'SIRCA.NS', 
'SIS.NS', 
'SITINET.NS', 
'SIYSIL.NS', 
'SJS.NS', 
'SJVN.NS', 
'SKFINDIA.NS', 
'SKIL.NS', 
'SKIPPER.NS', 
'SKMEGGPROD.NS', 
'SKP.NS', 
'SKSTEXTILE.NS', 
'SMARTLINK.NS', 
'SMCGLOBAL.NS', 
'SMLISUZU.NS', 
'SMLT.NS', 
'SMSLIFE.NS', 
'SMSPHARMA.NS', 
'SMVD.NS', 
'SNOWMAN.NS', 
'SOBHA.NS', 
'SOFTTECH.NS', 
'SOLARA.NS', 
'SOLARINDS.NS', 
'SOLEX.NS', 
'SOMANYCERA.NS', 
'SOMATEX.NS', 
'SOMICONVEY.NS', 
'SONACOMS.NS', 
'SONAHISONA.NS', 
'SONAMCLOCK.NS', 
'SONATSOFTW.NS', 
'SONISOYA.NS', 
'SONUINFRA.NS', 
'SOTL.NS', 
'SOUTHBANK.NS', 
'SOUTHWEST.NS', 
'SPAL.NS', 
'SPANDANA.NS', 
'SPARC.NS', 
'SPCENET.NS', 
'SPECIALITY.NS', 
'SPECTRUM.NS', 
'SPENCERS.NS', 
'SPENTEX.NS', 
'SPIC.NS', 
'SPLIL.NS', 
'SPLPETRO.NS', 
'SPMLINFRA.NS', 
'SPORTKING.NS', 
'SPRL.NS', 
'SPTL.NS', 
'SPYL.NS', 
'SREEL.NS', 
'SREINFRA.NS', 
'SRF.NS', 
'SRHHYPOLTD.NS', 
'SRIRAM.NS', 
'SRPL.NS', 
'SSINFRA.NS', 
'SSWL.NS', 
'STAMPEDE.NS', 
'STAR.NS', 
'STARCEMENT.NS', 
'STARHEALTH.NS', 
'STARPAPER.NS', 
'STARTECK.NS', 
'STCINDIA.NS', 
'STEELCAS.NS', 
'STEELCITY.NS', 
'STEELXIND.NS', 
'STEL.NS', 
'STERLINBIO.NS', 
'STERTOOLS.NS', 
'STLTECH.NS', 
'STOVEKRAFT.NS', 
'STYLAMIND.NS', 
'SUBCAPCITY.NS', 
'SUBEXLTD.NS', 
'SUBROS.NS', 
'SUDARSCHEM.NS', 
'SUKHJITS.NS', 
'SULA.NS', 
'SUMEETINDS.NS', 
'SUMICHEM.NS', 
'SUMIT.NS', 
'SUMMITSEC.NS', 
'SUNCLAYLTD.NS', 
'SUNDARAM.NS', 
'SUNDARMFIN.NS', 
'SUNDARMHLD.NS', 
'SUNDRMBRAK.NS', 
'SUNDRMFAST.NS', 
'SUNFLAG.NS', 
'SUNPHARMA.NS', 
'SUNTECK.NS', 
'SUNTV.NS', 
'SUPERHOUSE.NS', 
'SUPERSPIN.NS', 
'SUPRAJIT.NS', 
'SUPREMEENG.NS', 
'SUPREMEIND.NS', 
'SUPREMEINF.NS', 
'SUPRIYA.NS', 
'SURANASOL.NS', 
'SURANAT&P.NS', 
'SURANI.NS', 
'SURYALAXMI.NS', 
'SURYAROSNI.NS', 
'SURYODAY.NS', 
'SUTLEJTEX.NS', 
'SUULD.NS', 
'SUVEN.NS', 
'SUVENPHAR.NS', 
'SUVIDHAA.NS', 
'SUZLON.NS', 
'SVLL.NS', 
'SVPGLOB.NS', 
'SWANENERGY.NS', 
'SWARAJ.NS', 
'SWARAJENG.NS', 
'SWASTIK.NS', 
'SWELECTES.NS', 
'SWSOLAR.NS', 
'SYMPHONY.NS', 
'SYNCOMF.NS', 
'SYNGENE.NS', 
'SYRMA.NS', 
'TAINWALCHM.NS', 
'TAJGVK.NS', 
'TAKE.NS', 
'TALBROAUTO.NS', 
'TALWALKARS.NS', 
'TALWGYM.NS', 
'TANLA.NS', 
'TANTIACONS.NS', 
'TAPIFRUIT.NS', 
'TARACHAND.NS', 
'TARAPUR.NS', 
'TARC.NS', 
'TARMAT.NS', 
'TARSONS.NS', 
'TASTYBITE.NS', 
'TATACHEM.NS', 
'TATACOFFEE.NS', 
'TATACOMM.NS', 
'TATACONSUM.NS', 
'TATAELXSI.NS', 
'TATAINVEST.NS', 
'TATAMETALI.NS', 
'TATAMOTORS.NS', 
'TATAPOWER.NS', 
'TATASTEEL.NS', 
'TATASTLLP.NS', 
'TATVA.NS', 
'TBZ.NS', 
'TCI.NS', 
'TCIEXP.NS', 
'TCIFINANCE.NS', 
'TCNSBRANDS.NS', 
'TCPLPACK.NS', 
'TCS.NS', 
'TDPOWERSYS.NS', 
'TEAMLEASE.NS', 
'TECHIN.NS', 
'TECHM.NS', 
'TECHNOE.NS', 
'TECHNOFAB.NS', 
'TECILCHEM.NS', 
'TEGA.NS', 
'TEJASNET.NS', 
'TEMBO.NS', 
'TERASOFT.NS', 
'TEXINFRA.NS', 
'TEXMOPIPES.NS', 
'TEXRAIL.NS', 
'TFCILTD.NS', 
'TFL.NS', 
'TGBHOTELS.NS', 
'THANGAMAYL.NS', 
'THEINVEST.NS', 
'THEJO.NS', 
'THEMISMED.NS', 
'THERMAX.NS', 
'THIRUSUGAR.NS', 
'THOMASCOOK.NS', 
'THOMASCOTT.NS', 
'THYROCARE.NS', 
'TI.NS', 
'TIDEWATER.NS', 
'TIIL.NS', 
'TIINDIA.NS', 
'TIJARIA.NS', 
'TIL.NS', 
'TIMESCAN.NS', 
'TIMESGTY.NS', 
'TIMETECHNO.NS', 
'TIMKEN.NS', 
'TINPLATE.NS', 
'TIPSFILMS.NS', 
'TIPSINDLTD.NS', 
'TIRUMALCHM.NS', 
'TIRUPATI.NS', 
'TIRUPATIFL.NS', 
'TITAN.NS', 
'TMB.NS', 
'TNPETRO.NS', 
'TNPL.NS', 
'TNTELE.NS', 
'TOKYOPLAST.NS', 
'TORNTPHARM.NS', 
'TORNTPOWER.NS', 
'TOTAL.NS', 
'TOUCHWOOD.NS', 
'TPLPLASTEH.NS', 
'TRACXN.NS', 
'TRANSWIND.NS', 
'TREEHOUSE.NS', 
'TREJHARA.NS', 
'TRENT.NS', 
'TRF.NS', 
'TRIDENT.NS', 
'TRIGYN.NS', 
'TRIL.NS', 
'TRITURBINE.NS', 
'TRIVENI.NS', 
'TTKHLTCARE.NS', 
'TTKPRESTIG.NS', 
'TTL.NS', 
'TTML.NS', 
'TULSI.NS', 
'TV18BRDCST.NS', 
'TVSELECT.NS', 
'TVSMOTOR.NS', 
'TVSSRICHAK.NS', 
'TVTODAY.NS', 
'TVVISION.NS', 
'TWL.NS', 
'UBL.NS', 
'UCALFUEL.NS', 
'UCL.NS', 
'UCOBANK.NS', 
'UFLEX.NS', 
'UFO.NS', 
'UGARSUGAR.NS', 
'UGROCAP.NS', 
'UJAAS.NS', 
'UJJIVAN.NS', 
'UJJIVANSFB.NS', 
'ULTRACEMCO.NS', 
'UMA.NS', 
'UMAEXPORTS.NS', 
'UMANGDAIRY.NS', 
'UMESLTD.NS', 
'UNICHEMLAB.NS', 
'UNIDT.NS', 
'UNIENTER.NS', 
'UNIINFO.NS', 
'UNIONBANK.NS', 
'UNIPARTS.NS', 
'UNIPLY.NS', 
'UNITECH.NS', 
'UNITEDPOLY.NS', 
'UNITEDTEA.NS', 
'UNITY.NS', 
'UNIVAFOODS.NS', 
'UNIVASTU.NS', 
'UNIVCABLES.NS', 
'UNIVPHOTO.NS', 
'UNOMINDA.NS', 
'UPL.NS', 
'URAVI.NS', 
'URJA.NS', 
'USASEEDS.NS', 
'USHAMART.NS', 
'UTIAMC.NS', 
'UTTAMSUGAR.NS', 
'UWCSL.NS', 
'V2RETAIL.NS', 
'VADILALIND.NS', 
'VAIBHAVGBL.NS', 
'VAISHALI.NS', 
'VAKRANGEE.NS', 
'VALECHAENG.NS', 
'VALIANTORG.NS', 
'VALUEIND.NS', 
'VARDHACRLC.NS', 
'VARDMNPOLY.NS', 
'VARROC.NS', 
'VASA.NS', 
'VASCONEQ.NS', 
'VASWANI.NS', 
'VBL.NS', 
'VCL.NS', 
'VEDL.NS', 
'VEEKAYEM.NS', 
'VENKEYS.NS', 
'VENUSPIPES.NS', 
'VENUSREM.NS', 
'VERA.NS', 
'VERANDA.NS', 
'VERTOZ.NS', 
'VESUVIUS.NS', 
'VETO.NS', 
'VGUARD.NS', 
'VHL.NS', 
'VICEROY.NS', 
'VIDEOIND.NS', 
'VIDHIING.NS', 
'VIJAYA.NS', 
'VIJIFIN.NS', 
'VIKASECO.NS', 
'VIKASLIFE.NS', 
'VIMTALABS.NS', 
'VINATIORGA.NS', 
'VINDHYATEL.NS', 
'VINEETLAB.NS', 
'VINNY.NS', 
'VINYLINDIA.NS', 
'VIPCLOTHNG.NS', 
'VIPIND.NS', 
'VIPULLTD.NS', 
'VISAKAIND.NS', 
'VISASTEEL.NS', 
'VISESHINFO.NS', 
'VISHNU.NS', 
'VISHWARAJ.NS', 
'VISUINTL.NS', 
'VITAL.NS', 
'VIVIANA.NS', 
'VIVIDHA.NS', 
'VIVIMEDLAB.NS', 
'VIVO.NS', 
'VLSFINANCE.NS', 
'VMARCIND.NS', 
'VMART.NS', 
'VOLTAMP.NS', 
'VOLTAS.NS', 
'VRLLOG.NS', 
'VSCL.NS', 
'VSSL.NS', 
'VSTIND.NS', 
'VSTTILLERS.NS', 
'VTL.NS', 
'WABAG.NS', 
'WALCHANNAG.NS', 
'WALPAR.NS', 
'WANBURY.NS', 
'WEALTH.NS', 
'WEBELSOLAR.NS', 
'WEIZMANIND.NS', 
'WEL.NS', 
'WELCORP.NS', 
'WELENT.NS', 
'WELINV.NS', 
'WELSPUNIND.NS', 
'WENDT.NS', 
'WEWIN.NS', 
'WHEELS.NS', 
'WHIRLPOOL.NS', 
'WILLAMAGOR.NS', 
'WINDLAS.NS', 
'WINDMACHIN.NS', 
'WINSOME.NS', 
'WIPL.NS', 
'WIPRO.NS', 
'WOCKPHARMA.NS', 
'WONDERLA.NS', 
'WORTH.NS', 
'WSI.NS', 
'WSTCSTPAPR.NS', 
'XCHANGING.NS', 
'XELPMOC.NS', 
'XPROINDIA.NS', 
'YAARI.NS', 
'YESBANK.NS', 
'YUKEN.NS', 
'ZEEL.NS', 
'ZEELEARN.NS', 
'ZEEMEDIA.NS', 
'ZENITHEXPO.NS', 
'ZENITHSTL.NS', 
'ZENSARTECH.NS', 
'ZENTEC.NS', 
'ZFCVINDIA.NS', 
'ZICOM.NS', 
'ZIMLAB.NS', 
'ZODIAC.NS', 
'ZODIACLOTH.NS', 
'ZOMATO.NS', 
'ZOTA.NS', 
'ZUARI.NS', 
'ZUARIIND.NS', 
'ZYDUSLIFE.NS', 
'ZYDUSWELL.NS')
selected_stock = st.selectbox('Select dataset for prediction', stocks)

n_years = st.slider('Years of prediction:', 1, 4)
period = n_years * 365


@st.cache
def load_data(ticker):
    data = yf.download(ticker, START, TODAY)
    data.reset_index(inplace=True)
    return data

	
data_load_state = st.text('Loading data...')
data = load_data(selected_stock)
data_load_state.text('Loading data... done!')

st.subheader('Raw data')
st.write(data.tail())

# Plot raw data
def plot_raw_data():
	fig = go.Figure()
	fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name="stock_open"))
	fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="stock_close"))
	fig.layout.update(title_text='Time Series data with Rangeslider', xaxis_rangeslider_visible=True)
	st.plotly_chart(fig)
	
plot_raw_data()

# Predict forecast with Prophet.
df_train = data[['Date','Close']]
# df_train['Date'] = pd.to_datetime(df_train['Date'], format='%Y-%m-%d')
df_train['Date'] = df_train['Date'].dt.tz_localize(None)
df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

m = Prophet()
m.fit(df_train)
future = m.make_future_dataframe(periods=period)
forecast = m.predict(future)

# Show and plot forecast
st.subheader('Forecast data')
st.write(forecast.tail())
    
st.write(f'Forecast plot for {n_years} years')
fig1 = plot_plotly(m, forecast)
st.plotly_chart(fig1)

st.write("Forecast components")
fig2 = m.plot_components(forecast)
st.write(fig2)

# hide stuff for production deployment.
# Comment the following lines to enable debug 
# mode for the dev build
hide_debug_info = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            .viewerBadge_container__1QSob {visibility: hidden;}
            .viewerBadge_link__1S137 {visibility: hidden;}
            </style>
            """
st.markdown(hide_debug_info, unsafe_allow_html=True) 
