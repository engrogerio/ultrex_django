# Generated by Django 3.0.5 on 2020-04-15 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade',
            name='asset',
            field=models.CharField(choices=[('EURUSD', 'EURUSD'), ('EURGBP', 'EURGBP'), ('GBPJPY', 'GBPJPY'), ('EURJPY', 'EURJPY'), ('GBPUSD', 'GBPUSD'), ('USDJPY', 'USDJPY'), ('AUDCAD', 'AUDCAD'), ('NZDUSD', 'NZDUSD'), ('USDRUB', 'USDRUB'), ('AMAZON', 'AMAZON'), ('APPLE', 'APPLE'), ('BAIDU', 'BAIDU'), ('CISCO', 'CISCO'), ('FACEBOOK', 'FACEBOOK'), ('GOOGLE', 'GOOGLE'), ('INTEL', 'INTEL'), ('MSFT', 'MSFT'), ('YAHOO', 'YAHOO'), ('AIG', 'AIG'), ('CITI', 'CITI'), ('COKE', 'COKE'), ('GE', 'GE'), ('GM', 'GM'), ('GS', 'GS'), ('JPM', 'JPM'), ('MCDON', 'MCDON'), ('MORSTAN', 'MORSTAN'), ('NIKE', 'NIKE'), ('USDCHF', 'USDCHF'), ('XAUUSD', 'XAUUSD'), ('XAGUSD', 'XAGUSD'), ('EURUSD-OTC', 'EURUSD-OTC'), ('EURGBP-OTC', 'EURGBP-OTC'), ('USDCHF-OTC', 'USDCHF-OTC'), ('EURJPY-OTC', 'EURJPY-OTC'), ('NZDUSD-OTC', 'NZDUSD-OTC'), ('GBPUSD-OTC', 'GBPUSD-OTC'), ('USDJPY-OTC', 'USDJPY-OTC'), ('AUDCAD-OTC', 'AUDCAD-OTC'), ('ALIBABA', 'ALIBABA'), ('YANDEX', 'YANDEX'), ('AUDUSD', 'AUDUSD'), ('USDCAD', 'USDCAD'), ('AUDJPY', 'AUDJPY'), ('GBPCAD', 'GBPCAD'), ('GBPCHF', 'GBPCHF'), ('GBPAUD', 'GBPAUD'), ('EURCAD', 'EURCAD'), ('CHFJPY', 'CHFJPY'), ('CADCHF', 'CADCHF'), ('EURAUD', 'EURAUD'), ('TWITTER', 'TWITTER'), ('FERRARI', 'FERRARI'), ('TESLA', 'TESLA'), ('USDNOK', 'USDNOK'), ('EURNZD', 'EURNZD'), ('USDSEK', 'USDSEK'), ('USDTRY', 'USDTRY'), ('MMM:US', 'MMM:US'), ('ABT:US', 'ABT:US'), ('ABBV:US', 'ABBV:US'), ('ACN:US', 'ACN:US'), ('ATVI:US', 'ATVI:US'), ('ADBE:US', 'ADBE:US'), ('AAP:US', 'AAP:US'), ('AA:US', 'AA:US'), ('AGN:US', 'AGN:US'), ('MO:US', 'MO:US'), ('AMGN:US', 'AMGN:US'), ('T:US', 'T:US'), ('ADSK:US', 'ADSK:US'), ('BAC:US', 'BAC:US'), ('BBY:US', 'BBY:US'), ('BA:US', 'BA:US'), ('BMY:US', 'BMY:US'), ('CAT:US', 'CAT:US'), ('CTL:US', 'CTL:US'), ('CVX:US', 'CVX:US'), ('CTAS:US', 'CTAS:US'), ('CTXS:US', 'CTXS:US'), ('CL:US', 'CL:US'), ('CMCSA:US', 'CMCSA:US'), ('CXO:US', 'CXO:US'), ('COP:US', 'COP:US'), ('ED:US', 'ED:US'), ('COST:US', 'COST:US'), ('CVS:US', 'CVS:US'), ('DHI:US', 'DHI:US'), ('DHR:US', 'DHR:US'), ('DRI:US', 'DRI:US'), ('DVA:US', 'DVA:US'), ('DAL:US', 'DAL:US'), ('DVN:US', 'DVN:US'), ('DO:US', 'DO:US'), ('DLR:US', 'DLR:US'), ('DFS:US', 'DFS:US'), ('DISCA:US', 'DISCA:US'), ('DOV:US', 'DOV:US'), ('DTE:US', 'DTE:US'), ('DNB:US', 'DNB:US'), ('ETFC:US', 'ETFC:US'), ('EMN:US', 'EMN:US'), ('EBAY:US', 'EBAY:US'), ('ECL:US', 'ECL:US'), ('EIX:US', 'EIX:US'), ('EMR:US', 'EMR:US'), ('ETR:US', 'ETR:US'), ('EQT:US', 'EQT:US'), ('EFX:US', 'EFX:US'), ('EQR:US', 'EQR:US'), ('ESS:US', 'ESS:US'), ('EXPD:US', 'EXPD:US'), ('EXR:US', 'EXR:US'), ('XOM:US', 'XOM:US'), ('FFIV:US', 'FFIV:US'), ('FAST:US', 'FAST:US'), ('FRT:US', 'FRT:US'), ('FDX:US', 'FDX:US'), ('FIS:US', 'FIS:US'), ('FITB:US', 'FITB:US'), ('FSLR:US', 'FSLR:US'), ('FE:US', 'FE:US'), ('FISV:US', 'FISV:US'), ('FLS:US', 'FLS:US'), ('FMC:US', 'FMC:US'), ('FBHS:US', 'FBHS:US'), ('FCX:US', 'FCX:US'), ('FTR:US', 'FTR:US'), ('GILD:US', 'GILD:US'), ('HAS:US', 'HAS:US'), ('HON:US', 'HON:US'), ('IBM:US', 'IBM:US'), ('KHC:US', 'KHC:US'), ('LMT:US', 'LMT:US'), ('MA:US', 'MA:US'), ('MDT:US', 'MDT:US'), ('MU:US', 'MU:US'), ('NFLX:US', 'NFLX:US'), ('NEE:US', 'NEE:US'), ('NVDA:US', 'NVDA:US'), ('PYPL:US', 'PYPL:US'), ('PFE:US', 'PFE:US'), ('PM:US', 'PM:US'), ('PG:US', 'PG:US'), ('QCOM:US', 'QCOM:US'), ('DGX:US', 'DGX:US'), ('RTN:US', 'RTN:US'), ('CRM:US', 'CRM:US'), ('SLB:US', 'SLB:US'), ('SBUX:US', 'SBUX:US'), ('SYK:US', 'SYK:US'), ('DIS:US', 'DIS:US'), ('TWX:US', 'TWX:US'), ('VZ:US', 'VZ:US'), ('V:US', 'V:US'), ('WMT:US', 'WMT:US'), ('WBA:US', 'WBA:US'), ('WFC:US', 'WFC:US'), ('SNAP', 'SNAP'), ('DUBAI', 'DUBAI'), ('TA25', 'TA25'), ('AMD', 'AMD'), ('ALGN', 'ALGN'), ('ANSS', 'ANSS'), ('DRE', 'DRE'), ('IDXX', 'IDXX'), ('RMD', 'RMD'), ('SU', 'SU'), ('TFX', 'TFX'), ('TMUS', 'TMUS'), ('QQQ', 'QQQ'), ('SPY', 'SPY'), ('BTCUSD', 'BTCUSD'), ('XRPUSD', 'XRPUSD'), ('ETHUSD', 'ETHUSD'), ('LTCUSD', 'LTCUSD'), ('DSHUSD', 'DSHUSD'), ('BCHUSD', 'BCHUSD'), ('OMGUSD', 'OMGUSD'), ('ZECUSD', 'ZECUSD'), ('ETCUSD', 'ETCUSD'), ('BTCUSD-L', 'BTCUSD-L'), ('ETHUSD-L', 'ETHUSD-L'), ('LTCUSD-L', 'LTCUSD-L'), ('BCHUSD-L', 'BCHUSD-L'), ('BTGUSD', 'BTGUSD'), ('QTMUSD', 'QTMUSD'), ('XLMUSD', 'XLMUSD'), ('TRXUSD', 'TRXUSD'), ('EOSUSD', 'EOSUSD'), ('USDINR', 'USDINR'), ('USDPLN', 'USDPLN'), ('USDBRL', 'USDBRL'), ('USDZAR', 'USDZAR'), ('DBX', 'DBX'), ('SPOT', 'SPOT'), ('USDSGD', 'USDSGD'), ('USDHKD', 'USDHKD'), ('LLOYL-CHIX', 'LLOYL-CHIX'), ('VODL-CHIX', 'VODL-CHIX'), ('BARCL-CHIX', 'BARCL-CHIX'), ('TSCOL-CHIX', 'TSCOL-CHIX'), ('BPL-CHIX', 'BPL-CHIX'), ('HSBAL-CHIX', 'HSBAL-CHIX'), ('RBSL-CHIX', 'RBSL-CHIX'), ('BLTL-CHIX', 'BLTL-CHIX'), ('MRWL-CHIX', 'MRWL-CHIX'), ('STANL-CHIX', 'STANL-CHIX'), ('RRL-CHIX', 'RRL-CHIX'), ('MKSL-CHIX', 'MKSL-CHIX'), ('BATSL-CHIX', 'BATSL-CHIX'), ('ULVRL-CHIX', 'ULVRL-CHIX'), ('EZJL-CHIX', 'EZJL-CHIX'), ('ADSD-CHIX', 'ADSD-CHIX'), ('ALVD-CHIX', 'ALVD-CHIX'), ('BAYND-CHIX', 'BAYND-CHIX'), ('BMWD-CHIX', 'BMWD-CHIX'), ('CBKD-CHIX', 'CBKD-CHIX'), ('COND-CHIX', 'COND-CHIX'), ('DAID-CHIX', 'DAID-CHIX'), ('DBKD-CHIX', 'DBKD-CHIX'), ('DPWD-CHIX', 'DPWD-CHIX'), ('DTED-CHIX', 'DTED-CHIX'), ('EOAND-CHIX', 'EOAND-CHIX'), ('MRKD-CHIX', 'MRKD-CHIX'), ('SIED-CHIX', 'SIED-CHIX'), ('TKAD-CHIX', 'TKAD-CHIX'), ('VOW3D-CHIX', 'VOW3D-CHIX'), ('ENELM-CHIX', 'ENELM-CHIX'), ('ENIM-CHIX', 'ENIM-CHIX'), ('FCAM-CHIX', 'FCAM-CHIX'), ('PIRCM-CHIX', 'PIRCM-CHIX'), ('PSTM-CHIX', 'PSTM-CHIX'), ('TITM-CHIX', 'TITM-CHIX'), ('CSGNZ-CHIX', 'CSGNZ-CHIX'), ('NESNZ-CHIX', 'NESNZ-CHIX'), ('ROGZ-CHIX', 'ROGZ-CHIX'), ('UBSGZ-CHIX', 'UBSGZ-CHIX'), ('SANE-CHIX', 'SANE-CHIX'), ('BBVAE-CHIX', 'BBVAE-CHIX'), ('TEFE-CHIX', 'TEFE-CHIX'), ('AIRP-CHIX', 'AIRP-CHIX'), ('HEIOA-CHIX', 'HEIOA-CHIX'), ('ORP-CHIX', 'ORP-CHIX'), ('AUDCHF', 'AUDCHF'), ('AUDNZD', 'AUDNZD'), ('CADJPY', 'CADJPY'), ('EURCHF', 'EURCHF'), ('GBPNZD', 'GBPNZD'), ('NZDCAD', 'NZDCAD'), ('NZDJPY', 'NZDJPY'), ('EURNOK', 'EURNOK'), ('CHFSGD', 'CHFSGD'), ('EURSGD', 'EURSGD'), ('USDMXN', 'USDMXN'), ('JUVEM', 'JUVEM'), ('ASRM', 'ASRM'), ('MANU', 'MANU'), ('UKOUSD', 'UKOUSD'), ('XPTUSD', 'XPTUSD'), ('USOUSD', 'USOUSD'), ('W1', 'W1'), ('AUDDKK', 'AUDDKK'), ('AUDMXN', 'AUDMXN'), ('AUDNOK', 'AUDNOK'), ('AUDSEK', 'AUDSEK'), ('AUDSGD', 'AUDSGD'), ('AUDTRY', 'AUDTRY'), ('CADMXN', 'CADMXN'), ('CADNOK', 'CADNOK'), ('CADPLN', 'CADPLN'), ('CADTRY', 'CADTRY'), ('CHFDKK', 'CHFDKK'), ('CHFNOK', 'CHFNOK'), ('CHFSEK', 'CHFSEK'), ('CHFTRY', 'CHFTRY'), ('DKKPLN', 'DKKPLN'), ('DKKSGD', 'DKKSGD'), ('EURDKK', 'EURDKK'), ('EURMXN', 'EURMXN'), ('EURTRY', 'EURTRY'), ('EURZAR', 'EURZAR'), ('GBPILS', 'GBPILS'), ('GBPMXN', 'GBPMXN'), ('GBPNOK', 'GBPNOK'), ('GBPPLN', 'GBPPLN'), ('GBPSEK', 'GBPSEK'), ('GBPSGD', 'GBPSGD'), ('GBPTRY', 'GBPTRY'), ('NOKDKK', 'NOKDKK'), ('NOKJPY', 'NOKJPY'), ('NOKSEK', 'NOKSEK'), ('NZDDKK', 'NZDDKK'), ('NZDMXN', 'NZDMXN'), ('NZDNOK', 'NZDNOK'), ('NZDSEK', 'NZDSEK'), ('NZDSGD', 'NZDSGD'), ('NZDTRY', 'NZDTRY'), ('NZDZAR', 'NZDZAR'), ('PLNSEK', 'PLNSEK'), ('SEKDKK', 'SEKDKK'), ('SEKJPY', 'SEKJPY'), ('SGDJPY', 'SGDJPY'), ('USDDKK', 'USDDKK'), ('NZDCHF', 'NZDCHF'), ('GBPHUF', 'GBPHUF'), ('USDCZK', 'USDCZK'), ('USDHUF', 'USDHUF'), ('CADSGD', 'CADSGD'), ('EURCZK', 'EURCZK'), ('EURHUF', 'EURHUF'), ('USDTHB', 'USDTHB'), ('IOTUSD-L', 'IOTUSD-L'), ('XLMUSD-L', 'XLMUSD-L'), ('NEOUSD-L', 'NEOUSD-L'), ('ADAUSD-L', 'ADAUSD-L'), ('XEMUSD-L', 'XEMUSD-L'), ('XRPUSD-L', 'XRPUSD-L'), ('EEM', 'EEM'), ('FXI', 'FXI'), ('IWM', 'IWM'), ('GDX', 'GDX'), ('XOP', 'XOP'), ('XLK', 'XLK'), ('XLE', 'XLE'), ('XLU', 'XLU'), ('IEMG', 'IEMG'), ('XLY', 'XLY'), ('IYR', 'IYR'), ('SQQQ', 'SQQQ'), ('OIH', 'OIH'), ('SMH', 'SMH'), ('EWJ', 'EWJ'), ('XLB', 'XLB'), ('DIA', 'DIA'), ('TLT', 'TLT'), ('SDS', 'SDS'), ('EWW', 'EWW'), ('XME', 'XME'), ('JNUG', 'JNUG'), ('QID', 'QID'), ('AUS200', 'AUS200'), ('FRANCE40', 'FRANCE40'), ('GERMANY30', 'GERMANY30'), ('HONGKONG50', 'HONGKONG50'), ('SPAIN35', 'SPAIN35'), ('US30', 'US30'), ('USNDAQ100', 'USNDAQ100'), ('JAPAN225', 'JAPAN225'), ('USSPX500', 'USSPX500'), ('UK100', 'UK100'), ('TRXUSD-L', 'TRXUSD-L'), ('EOSUSD-L', 'EOSUSD-L'), ('BNBUSD-L', 'BNBUSD-L'), ('ACB', 'ACB'), ('CGC', 'CGC'), ('CRON', 'CRON'), ('GWPH', 'GWPH'), ('MJ', 'MJ'), ('TLRY', 'TLRY'), ('BUD', 'BUD'), ('LYFT', 'LYFT'), ('PINS', 'PINS'), ('ZM', 'ZM'), ('UBER', 'UBER'), ('MELI', 'MELI'), ('BYND', 'BYND'), ('BSVUSD-L', 'BSVUSD-L'), ('ONTUSD-L', 'ONTUSD-L'), ('ATOMUSD-L', 'ATOMUSD-L'), ('WORK', 'WORK'), ('FDJP', 'FDJP'), ('CAN', 'CAN'), ('VIAC', 'VIAC'), ('TFC', 'TFC')], max_length=20),
        ),
    ]
