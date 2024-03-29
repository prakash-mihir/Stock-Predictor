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

stocks = ('RELIANCE.NS', 
'TCS.NS', 
'HDFCBANK.NS', 
'INFY.NS', 
'ICICIBANK.NS', 
'HINDUNILVR.NS', 
'SBIN.NS', 
'HDFC.NS', 
'BHARTIARTL.NS', 
'ADANIENT.NS', 
'LICI.NS', 
'ITC.NS', 
'ATGL.NS', 
'BAJFINANCE.NS', 
'KOTAKBANK.NS', 
'ADANIGREEN.NS', 
'ASIANPAINT.NS', 
'LT.NS', 
'ADANITRANS.NS', 
'AXISBANK.NS', 
'HCLTECH.NS', 
'DMART.NS', 
'MARUTI.NS', 
'BAJAJFINSV.NS', 
'SUNPHARMA.NS', 
'TITAN.NS', 
'WIPRO.NS', 
'ULTRACEMCO.NS', 
'JSWSTEEL.NS', 
'ONGC.NS', 
'ADANIPORTS.NS', 
'NTPC.NS', 
'M&M.NS', 
'POWERGRID.NS', 
'COALINDIA.NS', 
'TATASTEEL.NS', 
'HINDZINC.NS', 
'PIDILITIND.NS', 
'LTIM.NS', 
'TATAMOTORS.NS', 
'SBILIFE.NS', 
'HDFCLIFE.NS', 
'ADANIPOWER.NS', 
'VEDL.NS', 
'GRASIM.NS', 
'IOC.NS', 
'HINDALCO.NS', 
'AMBUJACEM.NS', 
'BRITANNIA.NS', 
'BAJAJ-AUTO.NS', 
'SIEMENS.NS', 
'DABUR.NS', 
'TECHM.NS', 
'BANKBARODA.NS', 
'INDUSINDBK.NS', 
'DLF.NS', 
'DIVISLAB.NS', 
'GODREJCP.NS', 
'EICHERMOT.NS', 
'CIPLA.NS', 
'VBL.NS', 
'HAL.NS', 
'SHREECEM.NS', 
'AWL.NS', 
'INDIGO.NS', 
'SBICARD.NS', 
'BEL.NS', 
'BPCL.NS', 
'TATACONSUM.NS', 
'DRREDDY.NS', 
'HAVELLS.NS', 
'SRF.NS', 
'TATAPOWER.NS', 
'MARICO.NS', 
'ICICIPRULI.NS', 
'APOLLOHOSP.NS', 
'BAJAJHLDNG.NS', 
'MCDOWELL-N.NS', 
'GAIL.NS', 
'PNB.NS', 
'ICICIGI.NS', 
'IOB.NS', 
'CANBK.NS', 
'CHOLAFIN.NS', 
'YESBANK.NS', 
'JINDALSTEL.NS', 
'IDBI.NS', 
'ABB.NS', 
'BERGEPAINT.NS', 
'UNIONBANK.NS', 
'HEROMOTOCO.NS', 
'UPL.NS', 
'TIINDIA.NS', 
'LODHA.NS', 
'TORNTPHARM.NS', 
'PIIND.NS', 
'TVSMOTOR.NS', 
'INDUSTOWER.NS', 
'IRCTC.NS', 
'BOSCHLTD.NS', 
'NAUKRI.NS', 
'ZOMATO.NS', 
'MOTHERSON.NS', 
'TRENT.NS', 
'PAGEIND.NS', 
'JSWENERGY.NS', 
'PGHH.NS', 
'HDFCAMC.NS', 
'ACC.NS', 
'INDHOTEL.NS', 
'CONCOR.NS', 
'UBL.NS', 
'NYKAA.NS', 
'AUBANK.NS', 
'PATANJALI.NS', 
'SCHAEFFLER.NS', 
'MUTHOOTFIN.NS', 
'MAXHEALTH.NS', 
'IRFC.NS', 
'ZYDUSLIFE.NS', 
'ASHOKLEY.NS', 
'COLPAL.NS', 
'CGPOWER.NS', 
'BALKRISIND.NS', 
'BHARATFORG.NS', 
'NHPC.NS', 
'SOLARINDS.NS', 
'ASTRAL.NS', 
'TATAELXSI.NS', 
'LTTS.NS', 
'POLYCAB.NS', 
'CUMMINSIND.NS', 
'BANDHANBNK.NS', 
'UCOBANK.NS', 
'MRF.NS', 
'PFC.NS', 
'SHRIRAMFIN.NS', 
'MPHASIS.NS', 
'HONAUT.NS', 
'IDFCFIRSTB.NS', 
'TATACOMM.NS', 
'ABCAPITAL.NS', 
'BANKINDIA.NS', 
'NMDC.NS', 
'ALKEM.NS', 
'INDIANB.NS', 
'DALBHARAT.NS', 
'PAYTM.NS', 
'FLUOROCHEM.NS', 
'SAIL.NS', 
'GODREJPROP.NS', 
'JUBLFOOD.NS', 
'GUJGASLTD.NS', 
'LUPIN.NS', 
'HINDPETRO.NS', 
'STARHEALTH.NS', 
'MANYAVAR.NS', 
'PETRONET.NS', 
'OBEROIRLTY.NS', 
'BIOCON.NS', 
'GICRE.NS', 
'SUPREMEIND.NS', 
'RECLTD.NS', 
'APLAPOLLO.NS', 
'UNOMINDA.NS', 
'PERSISTENT.NS', 
'FEDERALBNK.NS', 
'LINDEINDIA.NS', 
'M&MFIN.NS', 
'IGL.NS', 
'ESCORTS.NS', 
'CENTRALBK.NS', 
'BHEL.NS', 
'ABFRL.NS', 
'DEEPAKNTR.NS', 
'VOLTAS.NS', 
'OFSS.NS', 
'COROMANDEL.NS', 
'GLAND.NS', 
'MSUMI.NS', 
'AUROPHARMA.NS', 
'SUNDARMFIN.NS', 
'PHOENIXLTD.NS', 
'IDEA.NS', 
'3MINDIA.NS', 
'SONACOMS.NS', 
'ATUL.NS', 
'SUMICHEM.NS', 
'AIAENG.NS', 
'FACT.NS', 
'DELHIVERY.NS', 
'METROBRAND.NS', 
'GMRINFRA.NS', 
'TATACHEM.NS', 
'COFORGE.NS', 
'KANSAINER.NS', 
'TORNTPOWER.NS', 
'POONAWALLA.NS', 
'SYNGENE.NS', 
'THERMAX.NS', 
'MFSL.NS', 
'TIMKEN.NS', 
'DIXON.NS', 
'ZEEL.NS', 
'PSB.NS', 
'LICHSGFIN.NS', 
'RELAXO.NS', 
'OIL.NS', 
'JKCEMENT.NS', 
'CRISIL.NS', 
'GLAXO.NS', 
'SKFINDIA.NS', 
'AARTIIND.NS', 
'DEVYANI.NS', 
'L&TFH.NS', 
'RAJESHEXPO.NS', 
'FORTIS.NS', 
'CROMPTON.NS', 
'IPCALAB.NS', 
'BATAINDIA.NS', 
'NIACL.NS', 
'APOLLOTYRE.NS', 
'MAHABANK.NS', 
'VINATIORGA.NS', 
'SUNDRMFAST.NS', 
'PFIZER.NS', 
'HATSUN.NS', 
'POLICYBZR.NS', 
'LAURUSLABS.NS', 
'NAVINFLUOR.NS', 
'PEL.NS', 
'GRINDWELL.NS', 
'ENDURANCE.NS', 
'KPITTECH.NS', 
'SUNTV.NS', 
'WHIRLPOOL.NS', 
'LALPATHLAB.NS', 
'EMAMILTD.NS', 
'PRESTIGE.NS', 
'KAJARIACER.NS', 
'BLUEDART.NS', 
'IIFL.NS', 
'TTML.NS', 
'FIVESTAR.NS', 
'KPRMILL.NS', 
'FINEORG.NS', 
'IRB.NS', 
'TRIDENT.NS', 
'BDL.NS', 
'ZFCVINDIA.NS', 
'CARBORUNIV.NS', 
'RAMCOCEM.NS', 
'GILLETTE.NS', 
'ISEC.NS', 
'MAZDOCK.NS', 
'CLEAN.NS', 
'IIFLWAM.NS', 
'NH.NS', 
'AJANTPHARM.NS', 
'NAM-INDIA.NS', 
'EXIDEIND.NS', 
'APTUS.NS', 
'JBCHEPHARM.NS', 
'GSPL.NS', 
'NATIONALUM.NS', 
'AAVAS.NS', 
'GODREJIND.NS', 
'AFFLE.NS', 
'CREDITACC.NS', 
'RVNL.NS', 
'POWERINDIA.NS', 
'REDINGTON.NS', 
'DCMSHRIRAM.NS', 
'BAJAJELEC.NS', 
'KIOCL.NS', 
'RATNAMANI.NS', 
'PPLPHARMA.NS', 
'ALKYLAMINE.NS', 
'RADICO.NS', 
'RHIM.NS', 
'SANOFI.NS', 
'SJVN.NS', 
'CUB.NS', 
'ELGIEQUIP.NS', 
'INDIAMART.NS', 
'CGCL.NS', 
'KEI.NS', 
'ABSLAMC.NS', 
'MAHINDCIE.NS', 
'NUVOCO.NS', 
'KALYANKJIL.NS', 
'IDFC.NS', 
'LAXMIMACH.NS', 
'HAPPSTMNDS.NS', 
'CHAMBLFERT.NS', 
'ASAHIINDIA.NS', 
'KEC.NS', 
'SFL.NS', 
'SUVENPHAR.NS', 
'CAMPUS.NS', 
'IEX.NS', 
'MEDANTA.NS', 
'JSL.NS', 
'KIMS.NS', 
'RENUKA.NS', 
'BASF.NS', 
'AEGISCHEM.NS', 
'CASTROLIND.NS', 
'GLENMARK.NS', 
'NLCINDIA.NS', 
'CDSL.NS', 
'FINPIPE.NS', 
'BLUESTARCO.NS', 
'ASTERDM.NS', 
'CENTURYPLY.NS', 
'VGUARD.NS', 
'APLLTD.NS', 
'TTKPRESTIG.NS', 
'EIHOTEL.NS', 
'GRINFRA.NS', 
'ANGELONE.NS', 
'UTIAMC.NS', 
'CAMS.NS', 
'BIKAJI.NS', 
'RBLBANK.NS', 
'BRIGADE.NS', 
'TATAINVEST.NS', 
'SUZLON.NS', 
'HINDCOPPER.NS', 
'PVR.NS', 
'AETHER.NS', 
'HUDCO.NS', 
'JSLHISAR.NS', 
'CHOLAHLDNG.NS', 
'GODFRYPHLP.NS', 
'NATCOPHARM.NS', 
'HFCL.NS', 
'MOTILALOFS.NS', 
'CESC.NS', 
'SUNCLAYLTD.NS', 
'AKZOINDIA.NS', 
'EIDPARRY.NS', 
'ALLCARGO.NS', 
'ITI.NS', 
'MRPL.NS', 
'MANAPPURAM.NS', 
'RAYMOND.NS', 
'AMARAJABAT.NS', 
'TANLA.NS', 
'JKLAKSHMI.NS', 
'ZYDUSWELL.NS', 
'GESHIP.NS', 
'VTL.NS', 
'VIPIND.NS', 
'KRBL.NS', 
'EASEMYTRIP.NS', 
'KARURVYSYA.NS', 
'DEEPAKFERT.NS', 
'GODREJAGRO.NS', 
'PNBHOUSING.NS', 
'CYIENT.NS', 
'TEJASNET.NS', 
'ERIS.NS', 
'BALAMINES.NS', 
'GALAXYSURF.NS', 
'GNFC.NS', 
'POLYMED.NS', 
'JINDWORLD.NS', 
'SAPPHIRE.NS', 
'JUBLINGREA.NS', 
'TRITURBINE.NS', 
'FINCABLES.NS', 
'KALPATPOWR.NS', 
'MGL.NS', 
'ASTRAZEN.NS', 
'BSOFT.NS', 
'RITES.NS', 
'BALRAMCHIN.NS', 
'SWANENERGY.NS', 
'CENTURYTEX.NS', 
'SHYAMMETL.NS', 
'SONATSOFTW.NS', 
'LXCHEM.NS', 
'SHOPERSTOP.NS', 
'ALOKINDS.NS', 
'GRANULES.NS', 
'WELSPUNIND.NS', 
'TMB.NS', 
'ROUTE.NS', 
'BIRLACORPN.NS', 
'LATENTVIEW.NS', 
'JYOTHYLAB.NS', 
'RAINBOW.NS', 
'SPLPETRO.NS', 
'SAREGAMA.NS', 
'RCF.NS', 
'PNCINFRA.NS', 
'BSE.NS', 
'CRAFTSMAN.NS', 
'MEDPLUS.NS', 
'EQUITASBNK.NS', 
'IBULHSGFIN.NS', 
'GRAPHITE.NS', 
'ANURAS.NS', 
'CHEMPLASTS.NS', 
'KNRCON.NS', 
'FSL.NS', 
'CHALET.NS', 
'CANFINHOME.NS', 
'GMMPFAUDLR.NS', 
'CCL.NS', 
'COCHINSHIP.NS', 
'STLTECH.NS', 
'NBCC.NS', 
'HGS.NS', 
'JKPAPER.NS', 
'NETWORK18.NS', 
'TCIEXP.NS', 
'APARINDS.NS', 
'JMFINANCIL.NS', 
'TRIVENI.NS', 
'METROPOLIS.NS', 
'BLS.NS', 
'LEMONTREE.NS', 
'CERA.NS', 
'INDIACEM.NS', 
'KSB.NS', 
'CEATLTD.NS', 
'BORORENEW.NS', 
'PRINCEPIPE.NS', 
'PGHL.NS', 
'PRAJIND.NS', 
'ECLERX.NS', 
'ACI.NS', 
'GOCOLORS.NS', 
'HOMEFIRST.NS', 
'GARFIBRES.NS', 
'ESABINDIA.NS', 
'AMBER.NS', 
'TV18BRDCST.NS', 
'SCI.NS', 
'SYMPHONY.NS', 
'BBTC.NS', 
'WELCORP.NS', 
'INDIGOPNTS.NS', 
'BEML.NS', 
'INOXLEISUR.NS', 
'QUESS.NS', 
'JBMA.NS', 
'INGERRAND.NS', 
'INTELLECT.NS', 
'EDELWEISS.NS', 
'JUBLPHARMA.NS', 
'BCG.NS', 
'GAEL.NS', 
'RTNINDIA.NS', 
'KFINTECH.NS', 
'SPARC.NS', 
'RAIN.NS', 
'SIS.NS', 
'DELTACORP.NS', 
'DATAPATTNS.NS', 
'MMTC.NS', 
'UJJIVANSFB.NS', 
'GUJALKALI.NS', 
'RUSTOMJEE.NS', 
'MAHLIFE.NS', 
'VMART.NS', 
'IRCON.NS', 
'RELIGARE.NS', 
'ORIENTELEC.NS', 
'MAPMYINDIA.NS', 
'GSFC.NS', 
'GRSE.NS', 
'RBA.NS', 
'SOBHA.NS', 
'J&KBANK.NS', 
'EPL.NS', 
'MHRIL.NS', 
'CAPLIPOINT.NS', 
'NCC.NS', 
'MAHSCOOTER.NS', 
'GPIL.NS', 
'PRSMJOHNSN.NS', 
'AVANTIFEED.NS', 
'USHAMART.NS', 
'MFL.NS', 
'JPPOWER.NS', 
'GLS.NS', 
'MASTEK.NS', 
'VAIBHAVGBL.NS', 
'VSTIND.NS', 
'SWSOLAR.NS', 
'JUSTDIAL.NS', 
'HIKAL.NS', 
'POLYPLEX.NS', 
'MTARTECH.NS', 
'SYRMA.NS', 
'LUXIND.NS', 
'ROLEXRINGS.NS', 
'PCBL.NS', 
'MINDACORP.NS', 
'RPOWER.NS', 
'GHCL.NS', 
'GPPL.NS', 
'JSWHL.NS', 
'SUNTECK.NS', 
'ZENSARTECH.NS', 
'CMSINFO.NS', 
'TCI.NS', 
'PARADEEP.NS', 
'VRLLOG.NS', 
'TATVA.NS', 
'KTKBANK.NS', 
'RALLIS.NS', 
'KIRLOSENG.NS', 
'GMDCLTD.NS', 
'SHARDACROP.NS', 
'STARCEMENT.NS', 
'ARVINDFASN.NS', 
'SUPRAJIT.NS', 
'PDSL.NS', 
'VARROC.NS', 
'JKTYRE.NS', 
'RAJRATAN.NS', 
'FDC.NS', 
'PRIVISCL.NS', 
'VIJAYA.NS', 
'INFIBEAM.NS', 
'ENGINERSIN.NS', 
'MASFIN.NS', 
'ICRA.NS', 
'IBREALEST.NS', 
'KAYNES.NS', 
'MAHSEAMLES.NS', 
'TEAMLEASE.NS', 
'NESCO.NS', 
'EQUITAS.NS', 
'AARTIDRUGS.NS', 
'HEIDELBERG.NS', 
'LAOPALA.NS', 
'HSCL.NS', 
'RKFORGE.NS', 
'NIITLTD.NS', 
'JAMNAAUTO.NS', 
'SPANDANA.NS', 
'BOROLTD.NS', 
'GREENPANEL.NS', 
'BHARATRAS.NS', 
'CSBBANK.NS', 
'PRUDENT.NS', 
'GREENLAM.NS', 
'ELECON.NS', 
'RAILTEL.NS', 
'MIDHANI.NS', 
'TATACOFFEE.NS', 
'OLECTRA.NS', 
'UFLEX.NS', 
'IONEXCHANG.NS', 
'HGINFRA.NS', 
'ROSSARI.NS', 
'HCG.NS', 
'SHAREINDIA.NS', 
'SAFARI.NS', 
'HEG.NS', 
'SCHNEIDER.NS', 
'DCBBANK.NS', 
'SANSERA.NS', 
'SOUTHBANK.NS', 
'NOCIL.NS', 
'PCJEWELLER.NS', 
'TEGA.NS', 
'NAZARA.NS', 
'NFL.NS', 
'BARBEQUE.NS', 
'INDOCO.NS', 
'DAAWAT.NS', 
'TARSONS.NS', 
'JTEKTINDIA.NS', 
'SARDAEN.NS', 
'FUSION.NS', 
'IFBIND.NS', 
'ANANTRAJ.NS', 
'RELINFRA.NS', 
'ACE.NS', 
'MAHLOG.NS', 
'TECHNOE.NS', 
'NAVA.NS', 
'JWL.NS', 
'ISGEC.NS', 
'AMIORG.NS', 
'TINPLATE.NS', 
'BANARISUG.NS', 
'JINDALPOLY.NS', 
'HARSHA.NS', 
'PAISALO.NS', 
'WSTCSTPAPR.NS', 
'ASTEC.NS', 
'DISHTV.NS', 
'GATEWAY.NS', 
'UJJIVAN.NS', 
'THOMASCOOK.NS', 
'DHANUKA.NS', 
'EMIL.NS', 
'JINDALSAW.NS', 
'MOIL.NS', 
'THYROCARE.NS', 
'VESUVIUS.NS', 
'GREAVESCOT.NS', 
'TCNSBRANDS.NS', 
'WOCKPHARMA.NS', 
'HINDWAREAP.NS', 
'DBREALTY.NS', 
'AHLUCONT.NS', 
'DBL.NS', 
'KKCL.NS', 
'STAR.NS', 
'ADVENZYMES.NS', 
'RESPONIND.NS', 
'MOLDTKPAC.NS', 
'NEOGEN.NS', 
'GRAVITA.NS', 
'RATEGAIN.NS', 
'DALMIASUG.NS', 
'CHENNPETRO.NS', 
'HEMIPROP.NS', 
'HATHWAY.NS', 
'TATASTLLP.NS', 
'SAGCEM.NS', 
'ITDC.NS', 
'HCC.NS', 
'IFCI.NS', 
'KSCL.NS', 
'INOXWIND.NS', 
'DODLA.NS', 
'RSYSTEMS.NS', 
'JCHAC.NS', 
'AUTOAXLES.NS', 
'MIRZAINT.NS', 
'GET&D.NS', 
'POWERMECH.NS', 
'MAITHANALL.NS', 
'VAKRANGEE.NS', 
'HBLPOWER.NS', 
'ANANDRATHI.NS', 
'GANESHHOUC.NS', 
'IPL.NS', 
'NAVNETEDUL.NS', 
'MOL.NS', 
'NILKAMAL.NS', 
'VOLTAMP.NS', 
'BUTTERFLY.NS', 
'FCL.NS', 
'SULA.NS', 
'MANINFRA.NS', 
'SUDARSCHEM.NS', 
'TASTYBITE.NS', 
'VENKEYS.NS', 
'TWL.NS', 
'GABRIEL.NS', 
'JAICORPLTD.NS', 
'SURYAROSNI.NS', 
'ICIL.NS', 
'SHANTIGEAR.NS', 
'OPTIEMUS.NS', 
'EVEREADY.NS', 
'UNIPARTS.NS', 
'GRMOVER.NS', 
'KIRLOSBROS.NS', 
'SHRIPISTON.NS', 
'TATAMETALI.NS', 
'PSPPROJECT.NS', 
'ORIENTCEM.NS', 
'NEWGEN.NS', 
'ASHOKA.NS', 
'CAMLINFINE.NS', 
'DHANI.NS', 
'WELENT.NS', 
'SSWL.NS', 
'CHOICEIN.NS', 
'ASTRAMICRO.NS', 
'EMUDHRA.NS', 
'BECTORFOOD.NS', 
'SIYSIL.NS', 
'JPASSOCIAT.NS', 
'BAJAJCON.NS', 
'KIRIINDUS.NS', 
'JAYNECOIND.NS', 
'GLOBUSSPR.NS', 
'APCOTEXIND.NS', 
'SHILPAMED.NS', 
'PGEL.NS', 
'PTC.NS', 
'MBAPL.NS', 
'DOLLAR.NS', 
'BSHSL.NS', 
'ETHOSLTD.NS', 
'INDIAGLYCO.NS', 
'TVSSRICHAK.NS', 
'MARKSANS.NS', 
'PARAS.NS', 
'SBCL.NS', 
'ARVIND.NS', 
'PRICOLLTD.NS', 
'DFMFOODS.NS', 
'JMCPROJECT.NS', 
'TIPSINDLTD.NS', 
'ELECTCAST.NS', 
'FIEMIND.NS', 
'HONDAPOWER.NS', 
'SEAMECLTD.NS', 
'BBOX.NS', 
'RUPA.NS', 
'NDTV.NS', 
'UNICHEMLAB.NS', 
'TIIL.NS', 
'PFOCUS.NS', 
'CONFIPET.NS', 
'GOKEX.NS', 
'INSECTICID.NS', 
'MAXVIL.NS', 
'BAJAJHIND.NS', 
'GUFICBIO.NS', 
'SHARDAMOTR.NS', 
'CARTRADE.NS', 
'IOLCP.NS', 
'DBCORP.NS', 
'SEQUENT.NS', 
'PURVA.NS', 
'GENUSPOWER.NS', 
'DCXINDIA.NS', 
'ACCELYA.NS', 
'LGBBROSLTD.NS', 
'NEULANDLAB.NS', 
'BALMLAWRIE.NS', 
'DIAMONDYD.NS', 
'RTNPOWER.NS', 
'PILANIINVS.NS', 
'KOLTEPATIL.NS', 
'AGI.NS', 
'FINOPB.NS', 
'PANAMAPET.NS', 
'SUNDARMHLD.NS', 
'COSMOFIRST.NS', 
'SOTL.NS', 
'AMRUTANJAN.NS', 
'GULFOILLUB.NS', 
'NACLIND.NS', 
'TIRUMALCHM.NS', 
'MSTCLTD.NS', 
'JKIL.NS', 
'ITDCEM.NS', 
'ATFL.NS', 
'FILATEX.NS', 
'WABAG.NS', 
'APOLLOPIPE.NS', 
'TIMETECHNO.NS', 
'JISLJALEQS.NS', 
'SUNFLAG.NS', 
'GANECOS.NS', 
'SOMANYCERA.NS', 
'HERANBA.NS', 
'MMFL.NS', 
'DWARKESH.NS', 
'RAMKY.NS', 
'MUKANDLTD.NS', 
'SHK.NS', 
'HIL.NS', 
'IIFLSEC.NS', 
'SUBROS.NS', 
'RILINFRA.NS', 
'CANTABIL.NS', 
'MOREPENLAB.NS', 
'WONDERLA.NS', 
'INDOSTAR.NS', 
'JAGRAN.NS', 
'STYLAMIND.NS', 
'SUBEXLTD.NS', 
'DREAMFOLKS.NS', 
'VSTTILLERS.NS', 
'VINDHYATEL.NS', 
'SUPRIYA.NS', 
'KIRLOSIND.NS', 
'VADILALIND.NS', 
'TI.NS', 
'SWARAJENG.NS', 
'GATI.NS', 
'KESORAMIND.NS', 
'TDPOWERSYS.NS', 
'SIRCA.NS', 
'LANDMARK.NS', 
'ALEMBICLTD.NS', 
'TEXRAIL.NS', 
'HINDOILEXP.NS', 
'GOCLCORP.NS', 
'MAYURUNIQ.NS', 
'ANDHRSUGAR.NS', 
'VIDHIING.NS', 
'CARERATING.NS', 
'VISHNU.NS', 
'GOKULAGRO.NS', 
'BEPL.NS', 
'SPIC.NS', 
'GREENPLY.NS', 
'SESHAPAPER.NS', 
'SANGHIIND.NS', 
'FMGOETZE.NS', 
'ORISSAMINE.NS', 
'TIDEWATER.NS', 
'FAIRCHEMOR.NS', 
'ADFFOODS.NS', 
'GENESYS.NS', 
'ANDHRAPAP.NS', 
'STOVEKRAFT.NS', 
'HERITGFOOD.NS', 
'DEN.NS', 
'DHAMPURSUG.NS', 
'MTNL.NS', 
'BOMDYEING.NS', 
'DATAMATICS.NS', 
'LUMAXTECH.NS', 
'SALASAR.NS', 
'SHALBY.NS', 
'AVTNPL.NS', 
'NELCO.NS', 
'TNPL.NS', 
'HMT.NS', 
'VALIANTORG.NS', 
'ISMTLTD.NS', 
'LSIL.NS', 
'IGPL.NS', 
'LUMAXIND.NS', 
'KPIGREEN.NS', 
'KSL.NS', 
'GTPL.NS', 
'KINGFA.NS', 
'KABRAEXTRU.NS', 
'INDORAMA.NS', 
'SOLARA.NS', 
'DYNAMATECH.NS', 
'JSWISPL.NS', 
'SPCENET.NS', 
'SHANKARA.NS', 
'GRWRHITECH.NS', 
'IMAGICAA.NS', 
'HESTERBIO.NS', 
'GTLINFRA.NS', 
'VERANDA.NS', 
'DCW.NS', 
'HUHTAMAKI.NS', 
'THANGAMAYL.NS', 
'SJS.NS', 
'GALLANTT.NS', 
'SUVEN.NS', 
'DCAL.NS', 
'ORCHPHARMA.NS', 
'WENDT.NS', 
'NRBBEARING.NS', 
'GOLDIAM.NS', 
'KCP.NS', 
'ZENTEC.NS', 
'ARVSMART.NS', 
'TVTODAY.NS', 
'BFUTILITIE.NS', 
'SHAILY.NS', 
'VENUSPIPES.NS', 
'KRSNAA.NS', 
'GNA.NS', 
'REPCOHOME.NS', 
'CIGNITITEC.NS', 
'EXCELINDUS.NS', 
'MONTECARLO.NS', 
'BANCOINDIA.NS', 
'ALICON.NS', 
'RIIL.NS', 
'IMFA.NS', 
'TTKHLTCARE.NS', 
'MPSLTD.NS', 
'OAL.NS', 
'SANGHVIMOV.NS', 
'MANALIPETC.NS', 
'RPGLIFE.NS', 
'ASHIANA.NS', 
'INOXGREEN.NS', 
'RAMASTEEL.NS', 
'GMRP&UI.NS', 
'TCPLPACK.NS', 
'RAMCOIND.NS', 
'PUNJABCHEM.NS', 
'WHEELS.NS', 
'BBL.NS', 
'SEPC.NS', 
'INEOSSTYRO.NS', 
'SASKEN.NS', 
'APTECHT.NS', 
'SANDHAR.NS', 
'BHAGCHEM.NS', 
'OMAXE.NS', 
'DBOL.NS', 
'KDDL.NS', 
'RPSGVENT.NS', 
'SATIA.NS', 
'GULPOLY.NS', 
'ORIENTHOT.NS', 
'MATRIMONY.NS', 
'SKIPPER.NS', 
'SAKSOFT.NS', 
'SURYODAY.NS', 
'TAJGVK.NS', 
'RANEHOLDIN.NS', 
'EIHAHOTELS.NS', 
'KITEX.NS', 
'INFOBEAN.NS', 
'DPSCLTD.NS', 
'KUANTUM.NS', 
'KRISHANA.NS', 
'SHRIRAMPPS.NS', 
'IGARASHI.NS', 
'CARYSIL.NS', 
'MADRASFERT.NS', 
'PRECWIRE.NS', 
'GIPCL.NS', 
'THEMISMED.NS', 
'TARC.NS', 
'VSSL.NS', 
'SATIN.NS', 
'FOSECOIND.NS', 
'EVERESTIND.NS', 
'EXPLEOSOL.NS', 
'BAJAJHCARE.NS', 
'ARMANFIN.NS', 
'MANORAMA.NS', 
'STEELXIND.NS', 
'THEJO.NS', 
'PARAGMILK.NS', 
'XPROINDIA.NS', 
'POKARNA.NS', 
'PIXTRANS.NS', 
'ROSSELLIND.NS', 
'NSIL.NS', 
'UGARSUGAR.NS', 
'ADORWELD.NS', 
'PNBGILTS.NS', 
'GICHSGFIN.NS', 
'GMBREW.NS', 
'NITINSPIN.NS', 
'AXISCADES.NS', 
'EKC.NS', 
'GEOJITFSL.NS', 
'ELIN.NS', 
'RICOAUTO.NS', 
'SHIVALIK.NS', 
'BFINVEST.NS', 
'AJMERA.NS', 
'UTTAMSUGAR.NS', 
'AVADHSUGAR.NS', 
'SANGAMIND.NS', 
'CHEMCON.NS', 
'ESTER.NS', 
'DREDGECORP.NS', 
'SPECIALITY.NS', 
'MONARCH.NS', 
'UGROCAP.NS', 
'MARATHON.NS', 
'CENTRUM.NS', 
'MEDICAMEQ.NS', 
'IWEL.NS', 
'MANGCHEFER.NS', 
'CAPACITE.NS', 
'PITTIENG.NS', 
'SHREDIGCEM.NS', 
'PFS.NS', 
'NUCLEUS.NS', 
'BIGBLOC.NS', 
'ARTEMISMED.NS', 
'SUTLEJTEX.NS', 
'NAHARSPING.NS', 
'COFFEEDAY.NS', 
'HITECH.NS', 
'GOODLUCK.NS', 
'CLOUD.NS', 
'JASH.NS', 
'BODALCHEM.NS', 
'SMLISUZU.NS', 
'AXITA.NS', 
'PRAKASH.NS', 
'PATELENG.NS', 
'JAGSNPHARM.NS', 
'STERTOOLS.NS', 
'VIMTALABS.NS', 
'KAMDHENU.NS', 
'ONMOBILE.NS', 
'AHL.NS', 
'UNIVCABLES.NS', 
'NAVKARCORP.NS', 
'NGLFINE.NS', 
'SHALPAINTS.NS', 
'IFGLEXPOR.NS', 
'5PAISA.NS', 
'PRECAM.NS', 
'SPORTKING.NS', 
'GEPIL.NS', 
'MKPL.NS', 
'SANDESH.NS', 
'VHL.NS', 
'ZEEMEDIA.NS', 
'QUICKHEAL.NS', 
'RGL.NS', 
'CENTUM.NS', 
'STEELCAS.NS', 
'ARIHANTSUP.NS', 
'UNIENTER.NS', 
'HARIOMPIPE.NS', 
'CENTENKA.NS', 
'VINYLINDIA.NS', 
'IMPAL.NS', 
'INDNIPPON.NS', 
'DEEPINDS.NS', 
'AGARIND.NS', 
'GANESHBE.NS', 
'SASTASUNDR.NS', 
'LIKHITHA.NS', 
'PGIL.NS', 
'RUSHIL.NS', 
'SRHHYPOLTD.NS', 
'HEXATRADEX.NS', 
'ORIENTPPR.NS', 
'ASHAPURMIN.NS', 
'PANACEABIO.NS', 
'RSWM.NS', 
'AWHCL.NS', 
'RADIOCITY.NS', 
'NELCAST.NS', 
'EMAMIPAP.NS', 
'AMBIKCO.NS', 
'ANUP.NS', 
'KOKUYOCMLN.NS', 
'JINDRILL.NS', 
'SDBL.NS', 
'SPAL.NS', 
'CLNINDIA.NS', 
'DVL.NS', 
'SIGACHI.NS', 
'SYNCOMF.NS', 
'KICL.NS', 
'MANGLMCEM.NS', 
'TNPETRO.NS', 
'JYOTISTRUC.NS', 
'HIMATSEIDE.NS', 
'GREENPOWER.NS', 
'JETAIRWAYS.NS', 
'SMCGLOBAL.NS', 
'TRACXN.NS', 
'NCLIND.NS', 
'JAIBALAJI.NS', 
'APCL.NS', 
'DLINKINDIA.NS', 
'AURIONPRO.NS', 
'RAMCOSYS.NS', 
'HLVLTD.NS', 
'ALLSEC.NS', 
'OCCL.NS', 
'AGSTRA.NS', 
'63MOONS.NS', 
'ASALCBR.NS', 
'BCLIND.NS', 
'APEX.NS', 
'ORIENTBELL.NS', 
'TEXINFRA.NS', 
'ZOTA.NS', 
'PENIND.NS', 
'SATINDLTD.NS', 
'INDRAMEDCO.NS', 
'KHAICHEM.NS', 
'BLISSGVS.NS', 
'INDIANHUME.NS', 
'SHAKTIPUMP.NS', 
'XCHANGING.NS', 
'VISAKAIND.NS', 
'TFCILTD.NS', 
'TRIL.NS', 
'RAMRAT.NS', 
'ENIL.NS', 
'VASCONEQ.NS', 
'BLKASHYAP.NS', 
'ROTO.NS', 
'KOPRAN.NS', 
'GFLLIMITED.NS', 
'RAJMET.NS', 
'ROHLTD.NS', 
'LINCOLN.NS', 
'BHAGERIA.NS', 
'CREATIVE.NS', 
'JAYBARMARU.NS', 
'TALBROAUTO.NS', 
'SMSPHARMA.NS', 
'CHEVIOT.NS', 
'KANORICHEM.NS', 
'DECCANCE.NS', 
'FAZE3Q.NS', 
'ZUARI.NS', 
'3IINFOLTD.NS', 
'HPAL.NS', 
'BETA.NS', 
'BINDALAGRO.NS', 
'SUMMITSEC.NS', 
'HERCULES.NS', 
'CLSEL.NS', 
'PARACABLES.NS', 
'DMCC.NS', 
'ONWARDTEC.NS', 
'DHARMAJ.NS', 
'BHARATWIRE.NS', 
'ARIHANTCAP.NS', 
'RML.NS', 
'SCPL.NS', 
'RUBYMILLS.NS', 
'GANDHITUBE.NS', 
'CONTROLPR.NS', 
'NRL.NS', 
'SUKHJITS.NS', 
'SHREYAS.NS', 
'NAHARPOLY.NS', 
'ASIANTILES.NS', 
'HPL.NS', 
'DPABHUSHAN.NS', 
'VIKASLIFE.NS', 
'INDOAMIN.NS', 
'DCMSRIND.NS', 
'SNOWMAN.NS', 
'YUKEN.NS', 
'DIGISPICE.NS', 
'ATULAUTO.NS', 
'REFEX.NS', 
'LINC.NS', 
'SCHAND.NS', 
'BALAXI.NS', 
'APOLLO.NS', 
'JUBLINDS.NS', 
'FOODSIN.NS', 
'SHREEPUSHK.NS', 
'SPENCERS.NS', 
'ASAL.NS', 
'ELDEHSG.NS', 
'KELLTONTEC.NS', 
'RBL.NS', 
'CREST.NS', 
'DPWIRES.NS', 
'UNIVPHOTO.NS', 
'JAYAGROGN.NS', 
'NECLIFE.NS', 
'WINDLAS.NS', 
'HCL-INSYS.NS', 
'STCINDIA.NS', 
'MENONBE.NS', 
'OSWALAGRO.NS', 
'MEDICO.NS', 
'TVSELECT.NS', 
'NAHARCAP.NS', 
'UNIDT.NS', 
'VLSFINANCE.NS', 
'EXXARO.NS', 
'HARDWYN.NS', 
'TBZ.NS', 
'URJA.NS', 
'HTMEDIA.NS', 
'SWELECTES.NS', 
'IFBAGRO.NS', 
'KSOLVES.NS', 
'DHANBANK.NS', 
'NRAIL.NS', 
'ADSL.NS', 
'NURECA.NS', 
'CSLFINANCE.NS', 
'RAMAPHO.NS', 
'HITECHGEAR.NS', 
'REPRO.NS', 
'SREEL.NS', 
'MANAKSIA.NS', 
'BBTCL.NS', 
'MUNJALAU.NS', 
'AARTISURF.NS', 
'GOACARBON.NS', 
'GENUSPAPER.NS', 
'PROZONINTU.NS', 
'INNOVANA.NS', 
'KRISHIVAL.NS', 
'ZIMLAB.NS', 
'GVKPIL.NS', 
'JPOLYINVST.NS', 
'UNITECH.NS', 
'FCSSOFT.NS', 
'SHYAMCENT.NS', 
'EQUIPPP.NS', 
'MANINDS.NS', 
'PLASTIBLEN.NS', 
'LIBERTSHOE.NS', 
'CONSOFINVT.NS', 
'MAGADSUGAR.NS', 
'SHEMAROO.NS', 
'BALAJITELE.NS', 
'PDMJEPAPER.NS', 
'THEINVEST.NS', 
'PREMEXPLN.NS', 
'DONEAR.NS', 
'HINDCOMPOS.NS', 
'DSSL.NS', 
'MAXIND.NS', 
'GSS.NS', 
'MUTHOOTCAP.NS', 
'VARDHACRLC.NS', 
'ZUARIIND.NS', 
'NAHARINDUS.NS', 
'MANORG.NS', 
'MIRCELECTR.NS', 
'SILVERTUC.NS', 
'INDOBORAX.NS', 
'ORBTEXP.NS', 
'DELPHIFX.NS', 
'KOTHARIPRO.NS', 
'MALLCOM.NS', 
'KECL.NS', 
'KHADIM.NS', 
'PTL.NS', 
'DEEPENR.NS', 
'GLOBAL.NS', 
'NXTDIGITAL.NS', 
'BGRENERGY.NS', 
'KRITI.NS', 
'KAYA.NS', 
'PONNIERODE.NS', 
'ORICONENT.NS', 
'SAKAR.NS', 
'DYCL.NS', 
'PARSVNATH.NS', 
'IRISDOREME.NS', 
'BIRLACABLE.NS', 
'INDSWFTLAB.NS', 
'RANASUG.NS', 
'SECL.NS', 
'MGEL.NS', 
'DHUNINV.NS', 
'HMVL.NS', 
'WEALTH.NS', 
'BANSWRAS.NS', 
'KOTHARIPET.NS', 
'MUNJALSHOW.NS', 
'VIPCLOTHNG.NS', 
'SAKUMA.NS', 
'CLEDUCATE.NS', 
'MOLDTECH.NS', 
'CHEMFAB.NS', 
'ICEMAKE.NS', 
'NBIFIN.NS', 
'MARINE.NS', 
'EIFFL.NS', 
'RITCO.NS', 
'SALZERELEC.NS', 
'OMINFRAL.NS', 
'PPL.NS', 
'MAWANASUG.NS', 
'GOKUL.NS', 
'HITECHCORP.NS', 
'KERNEX.NS', 
'AYMSYNTEX.NS', 
'4THDIM.NS', 
'ADVANIHOTR.NS', 
'MSPL.NS', 
'FROG.NS', 
'CYBERTECH.NS', 
'RUCHIRA.NS', 
'INTLCONV.NS', 
'KOTARISUG.NS', 
'LYKALABS.NS', 
'NDL.NS', 
'SKP.NS', 
'KCPSUGIND.NS', 
'HIRECT.NS', 
'SILINV.NS', 
'SARLAPOLY.NS', 
'SELAN.NS', 
'CUPID.NS', 
'PENINLAND.NS', 
'COOLCAPS.NS', 
'SVPGLOB.NS', 
'OSWALSEEDS.NS', 
'KNAGRI.NS', 
'HINDMOTORS.NS', 
'DYNPRO.NS', 
'LOYALTEX.NS', 
'RADHIKAJWE.NS', 
'JINDALPHOT.NS', 
'AURUM.NS', 
'V2RETAIL.NS', 
'DICIND.NS', 
'UFO.NS', 
'SHIVAMAUTO.NS', 
'MINDTECK.NS', 
'NDRAUTO.NS', 
'TAKE.NS', 
'SKMEGGPROD.NS', 
'VISHWARAJ.NS', 
'FOCE.NS', 
'WEBELSOLAR.NS', 
'DENORA.NS', 
'ORIENTABRA.NS', 
'HUBTOWN.NS', 
'CINELINE.NS', 
'PPAP.NS', 
'SERVOTECH.NS', 
'MACPOWER.NS', 
'BIRLAMONEY.NS', 
'BASML.NS', 
'REVATHI.NS', 
'GSCLCEMENT.NS', 
'INDOTHAI.NS', 
'DUCON.NS', 
'SOUTHWEST.NS', 
'BRNL.NS', 
'DUGLOBAL.NS', 
'SIMPLEXINF.NS', 
'GKWLIMITED.NS', 
'FOCUS.NS', 
'WEL.NS', 
'ASHIMASYN.NS', 
'VIKASECO.NS', 
'CHEMBOND.NS', 
'APOLSINHOT.NS', 
'JSLL.NS', 
'SBC.NS', 
'ALBERTDAVD.NS', 
'20MICRONS.NS', 
'KOTYARK.NS', 
'MMP.NS', 
'QMSMEDI.NS', 
'PRIMESECU.NS', 
'MEP.NS', 
'EMKAYTOOLS.NS', 
'GPTINFRA.NS', 
'ESSENTIA.NS', 
'GEECEE.NS', 
'SAKHTISUG.NS', 
'WALCHANNAG.NS', 
'BPL.NS', 
'MCLEODRUSS.NS', 
'ASAHISONG.NS', 
'BCONCEPTS.NS', 
'JITFINFRA.NS', 
'NATHBIOGEN.NS', 
'VITAL.NS', 
'AUTOIND.NS', 
'IEL.NS', 
'DCMNVL.NS', 
'EMAMIREAL.NS', 
'PASUPTAC.NS', 
'NIPPOBATRY.NS', 
'FCONSUMER.NS', 
'ONEPOINT.NS', 
'STEL.NS', 
'MAHEPC.NS', 
'STARPAPER.NS', 
'WINDMACHIN.NS', 
'TRIGYN.NS', 
'KMSUGAR.NS', 
'DANGEE.NS', 
'VERTOZ.NS', 
'RAJTV.NS', 
'PODDARMENT.NS', 
'LGBFORGE.NS', 
'DEVIT.NS', 
'ABAN.NS', 
'INDTERRAIN.NS', 
'EUROBOND.NS', 
'GINNIFILA.NS', 
'MHLXMIRU.NS', 
'UCALFUEL.NS', 
'EROSMEDIA.NS', 
'OSIAHYPER.NS', 
'SINTERCOM.NS', 
'ASIANENE.NS', 
'E2E.NS', 
'COASTCORP.NS', 
'BMETRICS.NS', 
'GRPLTD.NS', 
'GOYALALUM.NS', 
'MAZDA.NS', 
'JAYSREETEA.NS', 
'ARROWGREEN.NS', 
'SADBHAV.NS', 
'BROOKS.NS', 
'PAVNAIND.NS', 
'ARIES.NS', 
'NILAINFRA.NS', 
'SOLEX.NS', 
'SHIVAUM.NS', 
'MWL.NS', 
'MARALOVER.NS', 
'AARVI.NS', 
'AHLEAST.NS', 
'TOTAL.NS', 
'ACCURACY.NS', 
'USASEEDS.NS', 
'HARRMALAYA.NS', 
'BIL.NS', 
'PVP.NS', 
'CAREERP.NS', 
'TPLPLASTEH.NS', 
'SEJALLTD.NS', 
'KRITINUT.NS', 
'ZODIACLOTH.NS', 
'PIONDIST.NS', 
'DTIL.NS', 
'KILITCH.NS', 
'VENUSREM.NS', 
'KORE.NS', 
'MEGASOFT.NS', 
'UNITEDPOLY.NS', 
'REPL.NS', 
'BAFNAPH.NS', 
'SWASTIK.NS', 
'INSPIRISYS.NS', 
'KREBSBIO.NS', 
'PHANTOMFX.NS', 
'GUJAPOLLO.NS', 
'KAMATHOTEL.NS', 
'ANNAPURNA.NS', 
'MURUDCERA.NS', 
'ALLETEC.NS', 
'IVC.NS', 
'SINTEX.NS', 
'ZEELEARN.NS', 
'HDIL.NS', 
'MEGASTAR.NS', 
'PRECOT.NS', 
'EIMCOELECO.NS', 
'RAMANEWS.NS', 
'MAANALU.NS', 
'MANAKSTEEL.NS', 
'GIRRESORTS.NS', 
'SIL.NS', 
'SUPERHOUSE.NS', 
'INVENTURE.NS', 
'TIRUPATIFL.NS', 
'GULFPETRO.NS', 
'MBLINFRA.NS', 
'SPLIL.NS', 
'PRAXIS.NS', 
'MANGALAM.NS', 
'SUULD.NS', 
'SHREYANIND.NS', 
'MODISONLTD.NS', 
'SARVESHWAR.NS', 
'SADBHIN.NS', 
'AKSHARCHEM.NS', 
'ARSHIYA.NS', 
'BOHRAIND.NS', 
'SIGMA.NS', 
'VETO.NS', 
'AIRAN.NS', 
'VISESHINFO.NS', 
'PALREDTEC.NS', 
'VIPULLTD.NS', 
'SECURKLOUD.NS', 
'KOHINOOR.NS', 
'PREMIERPOL.NS', 
'ESSARSHPNG.NS', 
'MAHESHWARI.NS', 
'TIL.NS', 
'BSL.NS', 
'KANPRPLA.NS', 
'TIPSFILMS.NS', 
'JAINAM.NS', 
'ISFT.NS', 
'RAJSREESUG.NS', 
'RPPL.NS', 
'FLFL.NS', 
'LOVABLE.NS', 
'NITCO.NS', 
'BHARATGEAR.NS', 
'PILITA.NS', 
'BEDMUTHA.NS', 
'EMKAY.NS', 
'RNAVAL.NS', 
'INDOTECH.NS', 
'RUCHINFRA.NS', 
'XELPMOC.NS', 
'SGIL.NS', 
'MADHAVBAUG.NS', 
'SMSLIFE.NS', 
'TRF.NS', 
'LOKESHMACH.NS', 
'SMLT.NS', 
'IL&FSENGG.NS', 
'PAR.NS', 
'IITL.NS', 
'MAHAPEXLTD.NS', 
'TTL.NS', 
'ALMONDZ.NS', 
'ASPINWALL.NS', 
'ELGIRUBCO.NS', 
'PRITI.NS', 
'MODIRUBBER.NS', 
'KRISHNADEF.NS', 
'VISASTEEL.NS', 
'PASHUPATI.NS', 
'A2ZINFRA.NS', 
'SPTL.NS', 
'WORTH.NS', 
'AARON.NS', 
'COMPINFO.NS', 
'TIRUPATI.NS', 
'SIKKO.NS', 
'EMMBI.NS', 
'ANMOL.NS', 
'JOCIL.NS', 
'BYKE.NS', 
'ALPHAGEO.NS', 
'KBCGLOBAL.NS', 
'ZODIAC.NS', 
'CEREBRAINT.NS', 
'TEXMOPIPES.NS', 
'GOLDSTAR.NS', 
'RHFL.NS', 
'ARTNIRMAN.NS', 
'DJML.NS', 
'GOLDTECH.NS', 
'GAYAPROJ.NS', 
'GILLANDERS.NS', 
'OBCL.NS', 
'BEWLTD.NS', 
'WEIZMANIND.NS', 
'AKSHOPTFBR.NS', 
'UMAEXPORTS.NS', 
'WANBURY.NS', 
'YAARI.NS', 
'COMPUSOFT.NS', 
'ASCOM.NS', 
'LOTUSEYE.NS', 
'KAKATCEM.NS', 
'SHIVATEX.NS', 
'ASIANHOTNR.NS', 
'JMA.NS', 
'RANEENGINE.NS', 
'DCI.NS', 
'SETCO.NS', 
'INTENTECH.NS', 
'RVHL.NS', 
'3RDROCK.NS', 
'ALANKIT.NS', 
'ASTRON.NS', 
'DCM.NS', 
'INDOWIND.NS', 
'AKSHAR.NS', 
'URAVI.NS', 
'RPPINFRA.NS', 
'SURANAT&P.NS', 
'BALLARPUR.NS', 
'SITINET.NS', 
'IRIS.NS', 
'SVLL.NS', 
'AVROIND.NS', 
'SOFTTECH.NS', 
'VAISHALI.NS', 
'BTML.NS', 
'TEMBO.NS', 
'NOIDATOLL.NS', 
'JHS.NS', 
'ARCHIDPLY.NS', 
'KSHITIJPOL.NS', 
'INDBANK.NS', 
'BHAGYANGR.NS', 
'BALPHARMA.NS', 
'ARVEE.NS', 
'VINNY.NS', 
'NPST.NS', 
'PRITIKAUTO.NS', 
'RELCHEMQ.NS', 
'PROPEQUITY.NS', 
'STARTECK.NS', 
'SALONA.NS', 
'MANAKALUCO.NS', 
'PALASHSECU.NS', 
'AVG.NS', 
'UNITEDTEA.NS', 
'SMARTLINK.NS', 
'LEMERITE.NS', 
'LEXUS.NS', 
'NILASPACES.NS', 
'SHIGAN.NS', 
'REMSONSIND.NS', 
'PODDARHOUS.NS', 
'GENCON.NS', 
'NDGL.NS', 
'LASA.NS', 
'NIRAJ.NS', 
'INDIANCARD.NS', 
'UMANGDAIRY.NS', 
'CORALFINAC.NS', 
'IL&FSTRANS.NS', 
'SRPL.NS', 
'PANSARI.NS', 
'HILTON.NS', 
'AHLADA.NS', 
'ALPA.NS', 
'ALKALI.NS', 
'SUNDARAM.NS', 
'CAPTRUST.NS', 
'PARIN.NS', 
'IVP.NS', 
'BAHETI.NS', 
'SUNDRMBRAK.NS', 
'SALSTEEL.NS', 
'SHAHALLOYS.NS', 
'AJRINFRA.NS', 
'BLBLIMITED.NS', 
'SPECTRUM.NS', 
'GTL.NS', 
'NECCLTD.NS', 
'GANGESSECU.NS', 
'AIROLAM.NS', 
'ATLANTA.NS', 
'CCHHL.NS', 
'SPMLINFRA.NS', 
'NGIL.NS', 
'SECURCRED.NS', 
'KAPSTON.NS', 
'MUKTAARTS.NS', 
'AKG.NS', 
'GOLDENTOBC.NS', 
'OMAXAUTO.NS', 
'MANAKCOAT.NS', 
'DAMODARIND.NS', 
'MAHASTEEL.NS', 
'MRO-TEK.NS', 
'GAL.NS', 
'SIMBHALS.NS', 
'AMDIND.NS', 
'VMARCIND.NS', 
'FSC.NS', 
'PIONEEREMB.NS', 
'CTE.NS', 
'LPDC.NS', 
'SURYALAXMI.NS', 
'KRITIKA.NS', 
'AMJLAND.NS', 
'SIGIND.NS', 
'DRSDILIP.NS', 
'SURANASOL.NS', 
'ATALREAL.NS', 
'LAGNAM.NS', 
'LAMBODHARA.NS', 
'TARMAT.NS', 
'PRAENG.NS', 
'MOTOGENFIN.NS', 
'UNIVASTU.NS', 
'JAIPURKURT.NS', 
'FIBERWEB.NS', 
'SUVIDHAA.NS', 
'ANIKINDS.NS', 
'RKEC.NS', 
'TAINWALCHM.NS', 
'DIL.NS', 
'INCREDIBLE.NS', 
'PARTYCRUS.NS', 
'TOUCHWOOD.NS', 
'WELINV.NS', 
'GROBTEA.NS', 
'AUSOMENT.NS', 
'BAGFILMS.NS', 
'SONAMCLOCK.NS', 
'HPIL.NS', 
'IZMO.NS', 
'PRESSMN.NS', 
'AAREYDRUGS.NS', 
'SHRENIK.NS', 
'TOKYOPLAST.NS', 
'LLOYDS.NS', 
'SUMIT.NS', 
'STEELCITY.NS', 
'DGCONTENT.NS', 
'CELEBRITY.NS', 
'BEARDSELL.NS', 
'HINDCON.NS', 
'KANANIIND.NS', 
'ENERGYDEV.NS', 
'PROLIFE.NS', 
'VIVIMEDLAB.NS', 
'FIDEL.NS', 
'AGROPHOS.NS', 
'KALYANIFRG.NS', 
'ROML.NS', 
'BIOFILCHEM.NS', 
'ELECTHERM.NS', 
'AURDIS.NS', 
'PATINTLOG.NS', 
'PRAKASHSTL.NS', 
'GICL.NS', 
'DOLLEX.NS', 
'BHANDARI.NS', 
'ARCHIES.NS', 
'TARACHAND.NS', 
'MITCON.NS', 
'DBSTOCKBRO.NS', 
'MCL.NS', 
'SHIVAMILLS.NS', 
'MORARJEE.NS', 
'DHRUV.NS', 
'ANKITMETAL.NS', 
'CORDSCABLE.NS', 
'MHHL.NS', 
'TREJHARA.NS', 
'BANKA.NS', 
'OILCOUNTUB.NS', 
'DELTAMAGNT.NS', 
'ARIHANTACA.NS', 
'GSTL.NS', 
'CENTEXT.NS', 
'WIPL.NS', 
'SHREERAMA.NS', 
'FLEXITUFF.NS', 
'GEEKAYWIRE.NS', 
'NITIRAJ.NS', 
'PKTEA.NS', 
'EXCEL.NS', 
'AAATECH.NS', 
'ZENITHSTL.NS', 
'TREEHOUSE.NS', 
'KEYFINSERV.NS', 
'SAMBHAAV.NS', 
'GLOBALVECT.NS', 
'FEL.NS', 
'GIRIRAJ.NS', 
'AROGRANITE.NS', 
'LATTEYS.NS', 
'JBFIND.NS', 
'MAGNUM.NS', 
'AVSL.NS', 
'PANACHE.NS', 
'HISARMETAL.NS', 
'PIGL.NS', 
'AAKASH.NS', 
'PRECISION.NS', 
'SEPOWER.NS', 
'UMA.NS', 
'CMRSL.NS', 
'GLOBE.NS', 
'INDSWFTLTD.NS', 
'CINEVISTA.NS', 
'ORIENTLTD.NS', 
'REGENCERAM.NS', 
'NIDAN.NS', 
'ROLTA.NS', 
'MALUPAPER.NS', 
'SHRADHA.NS', 
'MAHICKRA.NS', 
'MDL.NS', 
'AGRITECH.NS', 
'RSSOFTWARE.NS', 
'MOKSH.NS', 
'MBECL.NS', 
'BANG.NS', 
'PENTAGOLD.NS', 
'AJOONI.NS', 
'HYBRIDFIN.NS', 
'IPSL.NS', 
'HOVS.NS', 
'ABMINTLLTD.NS', 
'HECPROJECT.NS', 
'VINEETLAB.NS', 
'BDR.NS', 
'PNC.NS', 
'UJAAS.NS', 
'ARHAM.NS', 
'SUPREMEINF.NS', 
'TERASOFT.NS', 
'PULZ.NS', 
'CUBEXTUB.NS', 
'VASWANI.NS', 
'AARVEEDEN.NS', 
'ACEINTEG.NS', 
'BVCL.NS', 
'RELIABLE.NS', 
'VIVIANA.NS', 
'KKVAPOW.NS', 
'MTEDUCARE.NS', 
'BANARBEADS.NS', 
'SUMEETINDS.NS', 
'NIBL.NS', 
'SIDDHIKA.NS', 
'AKASH.NS', 
'SANWARIA.NS', 
'LGHL.NS', 
'KHANDSE.NS', 
'ABCOTS.NS', 
'GANGAFORGE.NS', 
'WEWIN.NS', 
'SUPERSPIN.NS', 
'SOMICONVEY.NS', 
'NAGREEKEXP.NS', 
'TIMESCAN.NS', 
'MANUGRAPH.NS', 
'AISL.NS', 
'LIBAS.NS', 
'SGL.NS', 
'TIMESGTY.NS', 
'SAGARDEEP.NS', 
'JETFREIGHT.NS', 
'KHFM.NS', 
'AMBANIORG.NS', 
'BURNPUR.NS', 
'VSCL.NS', 
'GODHA.NS', 
'MRO.NS', 
'NEXTMEDIA.NS', 
'ARSSINFRA.NS', 
'DKEGL.NS', 
'PRITIKA.NS', 
'ADROITINFO.NS', 
'UCL.NS', 
'PARASPETRO.NS', 
'AGNI.NS', 
'ZENITHEXPO.NS', 
'VARDMNPOLY.NS', 
'BALKRISHNA.NS', 
'MADHUCON.NS', 
'RKDL.NS', 
'AMBICAAGAR.NS', 
'SONAHISONA.NS', 
'DNAMEDIA.NS', 
'MEGAFLEX.NS', 
'PEARLPOLY.NS', 
'MADHAV.NS', 
'SWARAJ.NS', 
'GOENKA.NS', 
'ICDSLTD.NS', 
'LAXMICOT.NS', 
'SANGINITA.NS', 
'DHARSUGAR.NS', 
'MARSHALL.NS', 
'SHAIVAL.NS', 
'HBSL.NS', 
'TGBHOTELS.NS', 
'JETKNIT.NS', 
'COUNCODOS.NS', 
'SHUBHLAXMI.NS', 
'JFLLIFE.NS', 
'FELIX.NS', 
'HEADSUP.NS', 
'CROWN.NS', 
'MINDPOOL.NS', 
'ADL.NS', 
'MILTON.NS', 
'VIVIDHA.NS', 
'KRIDHANINF.NS', 
'ROLLT.NS', 
'MERCATOR.NS', 
'KEEPLEARN.NS', 
'HAVISHA.NS', 
'OMKARCHEM.NS', 
'LFIC.NS', 
'UWCSL.NS', 
'NARMADA.NS', 
'AMEYA.NS', 
'RITEZONE.NS', 
'LCCINFOTEC.NS', 
'CALSOFT.NS', 
'SUPREMEENG.NS', 
'KARMAENG.NS', 
'SILLYMONKS.NS', 
'FMNL.NS', 
'SONUINFRA.NS', 
'EASTSILK.NS', 
'SOMATEX.NS', 
'3PLAND.NS', 
'QUADPRO.NS', 
'REXPIPES.NS', 
'CYBERMEDIA.NS', 
'CADSYS.NS', 
'VCL.NS', 
'EDUCOMP.NS', 
'MOXSH.NS', 
'WALPAR.NS', 
'OMFURN.NS', 
'SUBCAPCITY.NS', 
'CMICABLES.NS', 
'SILGO.NS', 
'INFOMEDIA.NS', 
'VIJIFIN.NS', 
'WILLAMAGOR.NS', 
'THOMASCOTT.NS', 
'JAKHARIA.NS', 
'VIVO.NS', 
'ASLIND.NS', 
'MPTODAY.NS', 
'DYNAMIC.NS', 
'ORIENTALTL.NS', 
'NKIND.NS', 
'TFL.NS', 
'RICHA.NS', 
'NAGREEKCAP.NS', 
'AMJUMBO.NS', 
'21STCENMGM.NS', 
'SHANTI.NS', 
'MASKINVEST.NS', 
'MOHITIND.NS', 
'KHAITANLTD.NS', 
'SABAR.NS', 
'UNIINFO.NS', 
'MAKS.NS', 
'TAPIFRUIT.NS', 
'TANTIACONS.NS', 
'GAYAHWS.NS', 
'SETUINFRA.NS', 
'VEEKAYEM.NS', 
'ISHAN.NS', 
'TIJARIA.NS', 
'ORTINLAB.NS', 
'GUJRAFFIA.NS', 
'ONELIFECAP.NS', 
'KAUSHALYA.NS', 
'VERA.NS', 
'METALFORGE.NS', 
'SURANI.NS', 
'LYPSAGEMS.NS', 
'MITTAL.NS', 
'TNTELE.NS', 
'AMIABLE.NS', 
'ABINFRA.NS', 
'SMVD.NS', 
'CONTI.NS', 
'NATNLSTEEL.NS', 
'TECHIN.NS', 
'RMCL.NS', 
'SPRL.NS', 
'JALAN.NS', 
'DESTINY.NS', 
'S&SPOWER.NS', 
'KAVVERITEL.NS', 
'KANDARP.NS', 
'PERFECT.NS', 
'ARENTERP.NS', 
'UMESLTD.NS', 
'ANTGRAPHIC.NS', 
'KALYANI.NS', 
'SSINFRA.NS', 
'SHYAMTEL.NS', 
'CMMIPL.NS', 
'ACCORD.NS', 
'TVVISION.NS', 
'RMDRIP.NS', 
'BRIGHT.NS', 
'DCMFINSERV.NS', 
'PREMIER.NS', 
'EUROTEXIND.NS', 
'RADAAN.NS', 
'KCK.NS', 
'NORBTEAEXP.NS', 
'SATHAISPAT.NS', 
'AILIMITED.NS', 
'CREATIVEYE.NS', 
'TARAPUR.NS', 
'ALPSINDUS.NS', 
'ABNINT.NS', 
'GLFL.NS', 
'VASA.NS', 
'BKMINDST.NS', 
'AHIMSA.NS', 
'GRETEX.NS', 
'SRIRAM.NS', 
'TRANSWIND.NS', 
'NIRAJISPAT.NS', 
'SKSTEXTILE.NS', 
'LAKPRE.NS', 
'SABEVENTS.NS', 
'INDLMETER.NS', 
'DRL.NS', 
'MANAV.NS', 
'BHALCHANDR.NS', 
'INNOVATIVE.NS', 
'MELSTAR.NS', 
'ABHISHEK.NS', 
'AHLWEST.NS', 
'AIFL.NS', 
'ALCHEM.NS', 
'ANDHRACEMT.NS', 
'ANSALAPI.NS', 
'ARCOTECH.NS', 
'ARTEDZ.NS', 
'ASIL.NS', 
'ATCOM.NS', 
'ATLASCYCLE.NS', 
'ATNINTER.NS', 
'AUTOLITIND.NS', 
'AUTORIDFIN.NS', 
'BANSAL.NS', 
'BARTRONICS.NS', 
'BGLOBAL.NS', 
'BHARATIDIL.NS', 
'BILENERGY.NS', 
'BINANIIND.NS', 
'BIRLATYRE.NS', 
'BLUEBLENDS.NS', 
'BLUECHIP.NS', 
'BLUECOAST.NS', 
'BRFL.NS', 
'CANDC.NS', 
'CCCL.NS', 
'CELESTIAL.NS', 
'CKFSL.NS', 
'CKPLEISURE.NS', 
'COX&KINGS.NS', 
'DIAPOWER.NS', 
'DIGJAMLMTD.NS', 
'DOLPHINOFF.NS', 
'DQE.NS', 
'DRCSYSTEMS.NS', 
'DSKULKARNI.NS', 
'EASTSUGIND.NS', 
'EASUNREYRL.NS', 
'EMCO.NS', 
'EON.NS', 
'EUROCERA.NS', 
'EUROMULTI.NS', 
'FEDDERELEC.NS', 
'FIVECORE.NS', 
'FRETAIL.NS', 
'GAMMONIND.NS', 
'GANGOTRI.NS', 
'GBGLOBAL.NS', 
'GFSTEELS.NS', 
'GISOLUTION.NS', 
'GITANJALI.NS', 
'HINDNATGLS.NS', 
'ICSA.NS', 
'IMPEXFERRO.NS', 
'INDOSOLAR.NS', 
'IVRCLINFRA.NS', 
'JAINSTUDIO.NS', 
'JIKIND.NS', 
'JINDCOT.NS', 
'JMTAUTOLTD.NS', 
'JPINFRATEC.NS', 
'KEERTI.NS', 
'KGL.NS', 
'KSERASERA.NS', 
'KSK.NS', 
'LAKSHMIEFL.NS', 
'LEEL.NS', 
'MANPASAND.NS', 
'MCDHOLDING.NS', 
'METKORE.NS', 
'MICEL.NS', 
'MODTHREAD.NS', 
'MOHOTAIND.NS', 
'MVL.NS', 
'NAGAFERT.NS', 
'NAKODA.NS', 
'NITINFIRE.NS', 
'NTL.NS', 
'NUTEK.NS', 
'OISL.NS', 
'OPAL.NS', 
'OPTOCIRCUI.NS', 
'ORTEL.NS', 
'PDPL.NS', 
'PINCON.NS', 
'POWERFUL.NS', 
'PRATIBHA.NS', 
'PRUDMOULI.NS', 
'PSL.NS', 
'PUNJLLOYD.NS', 
'QUINTEGRA.NS', 
'RAINBOWPAP.NS', 
'RAJRILTD.NS', 
'RAJVIR.NS', 
'RCOM.NS', 
'RELCAPITAL.NS', 
'RMMIL.NS', 
'RUSHABEAR.NS', 
'SABTN.NS', 
'SANCO.NS', 
'SBIHOMEFIN.NS', 
'SELMC.NS', 
'SEYAIND.NS', 
'SHARONBIO.NS', 
'SHIRPUR-G.NS', 
'SICAL.NS', 
'SIIL.NS', 
'SKIL.NS', 
'SONISOYA.NS', 
'SPENTEX.NS', 
'SPYL.NS', 
'SREINFRA.NS', 
'STAMPEDE.NS', 
'STERLINBIO.NS', 
'TALWALKARS.NS', 
'TALWGYM.NS', 
'TCIFINANCE.NS', 
'TECHNOFAB.NS', 
'TECILCHEM.NS', 
'THIRUSUGAR.NS', 
'TULSI.NS', 
'UNIPLY.NS', 
'UNITY.NS', 
'UNIVAFOODS.NS', 
'VALECHAENG.NS', 
'VALUEIND.NS', 
'VICEROY.NS', 
'VIDEOIND.NS', 
'VISUINTL.NS', 
'WINSOME.NS', 
'WSI.NS', 
'ZICOM.NS', )
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
try:
    df_train['Date'] = df_train['Date'].dt.tz_localize(None)
except(e):
    st.write('')

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
