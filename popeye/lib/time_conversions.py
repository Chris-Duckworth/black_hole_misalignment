'''Time conversions - convert between snapshot number, redshift and Gyrs'''

def snap_to_z(snapnum):
    '''
    Basically a dictionary which gives the redshift for a given snapshot.
    The function it was originally found from is here:

	def snap_to_z(basePath):
		  snaps = np.arange(0,100)
		  # Converting to include leading zeros.
		  formatter = "{:02d}".format
		  snaps = np.array(list(map(formatter,snaps)))
		  z = np.zeros(snaps.shape)
		  for ind,s in enumerate(snaps):
				  path = str(basePath)+'/snapdir_0'+str(s)+'/'
				  file = 'snap_0'+str(s)+'.0.hdf5'
				  tab = h5py.File(path+file)
				  tab_dict = dict(tab['Header'].attrs.items())
				  z[ind] = tab_dict['Redshift']
		  return z
		  
    This is quite slow to run every time you want to know the redshift, so using the 
    dictionary.    
    Disclaimer : There is probably an easier way of doing this that I have missed.       
    '''

    dict = {0: 20.046490988807516, 1: 14.989173240042412, 2: 11.980213315300293,
            3: 10.975643294137885, 4: 9.996590466186333, 5: 9.388771271940549, 
            6: 9.00233985416247, 7: 8.449476294368743, 8: 8.012172948865935, 
            9: 7.5951071498715965, 10: 7.23627606616736, 11: 7.005417045544533, 
            12: 6.491597745667503, 13: 6.0107573988449, 14: 5.846613747881867, 
            15: 5.5297658079491026, 16: 5.227580973127337, 17: 4.995933468164624, 
            18: 4.664517702470927, 19: 4.428033736605549, 20: 4.176834914726472, 
            21: 4.0079451114652676, 22: 3.7087742646422353, 23: 3.4908613692606485, 
            24: 3.2830330579565246, 25: 3.008131071630377, 26: 2.8957850057274284, 
            27: 2.7331426173187188, 28: 2.5772902716018935, 29: 2.4442257045541464, 
            30: 2.3161107439568918, 31: 2.207925472383703, 32: 2.1032696525957713, 
            33: 2.0020281392528516, 34: 1.9040895435327672, 35: 1.822689252620354, 
            36: 1.7435705743308647, 37: 1.6666695561144653, 38: 1.6042345220731056, 
            39: 1.5312390291576135, 40: 1.4955121664955557, 41: 1.4140982203725216, 
            42: 1.3575766674029972, 43: 1.3023784599059653, 44: 1.2484726142451428, 
            45: 1.2062580807810006, 46: 1.1546027123602154, 47: 1.1141505637653806, 
            48: 1.074457894547674, 49: 1.035510445664141, 50: 0.9972942257819404, 
            51: 0.9505313515850327, 52: 0.9230008161779089, 53: 0.8868969375752482, 
            54: 0.8514709006246495, 55: 0.8167099790118506, 56: 0.7910682489463392, 
            57: 0.7574413726158526, 58: 0.7326361820223115, 59: 0.7001063537185233, 
            60: 0.6761104112134777, 61: 0.6446418406845371, 62: 0.6214287452425136, 
            63: 0.5985432881875667, 64: 0.5759808451078874, 65: 0.5463921831410221, 
            66: 0.524565820433923, 67: 0.5030475232448832, 68: 0.4818329434209512, 
            69: 0.4609177941806475, 70: 0.4402978492477432, 71: 0.41996894199726653, 
            72: 0.3999269646135635, 73: 0.38016786726023866, 74: 0.36068765726181673, 
            75: 0.3478538418581776, 76: 0.32882972420595435, 77: 0.31007412012783386, 
            78: 0.2977176845174465, 79: 0.2733533465784399, 80: 0.2613432561610123, 
            81: 0.24354018155467028, 82: 0.22598838626019768, 83: 0.21442503551449454, 
            84: 0.19728418237600986, 85: 0.1803852617057493, 86: 0.1692520332436107, 
            87: 0.15274876890238098, 88: 0.14187620396956202, 89: 0.12575933241126092, 
            90: 0.10986994045882548, 91: 0.09940180263022191, 92: 0.08388443079747931, 
            93: 0.07366138465643868, 94: 0.058507322794512984, 95: 0.04852362998180593, 
            96: 0.0337243718735154, 97: 0.023974428382762536, 98: 0.009521666967944764, 
            99: 2.220446049250313e-16}
    return dict[snapnum]


def snap_to_scale_factor(snapnum):
    '''
    Basically a dictionary which gives the scale factor for a given snapshot.
    The function it was originally found from is here:

	def snap_to_z(basePath):
		  snaps = np.arange(0,100)
		  # Converting to include leading zeros.
		  formatter = "{:02d}".format
		  snaps = np.array(list(map(formatter,snaps)))
		  z = np.zeros(snaps.shape)
		  for ind,s in enumerate(snaps):
				  path = str(basePath)+'/snapdir_0'+str(s)+'/'
				  file = 'snap_0'+str(s)+'.0.hdf5'
				  tab = h5py.File(path+file)
				  tab_dict = dict(tab['Header'].attrs.items())
				  z[ind] = tab_dict['Redshift']
		  return z
		  
    This is quite slow to run every time you want to know the scale factor, so using the 
    dictionary.    
    Disclaimer : There is probably an easier way of doing this that I have missed. 
    '''

    dict = {0: 0.04751385874879561, 1: 0.06254232066831665, 2: 0.07704033637268967,
            3: 0.0835028211377591, 4: 0.09093727761117619, 5: 0.09625777426642748, 
            6: 0.09997660693201205, 7: 0.10582597054568338, 8: 0.11096103078290759, 
            9: 0.1163452627830171, 10: 0.12141409442402731, 11: 0.12491541593783131, 
            12: 0.1334828742744916, 13: 0.1426379409683697, 14: 0.14605760406878063, 
            15: 0.15314484920464314, 16: 0.1605759932010687, 17: 0.16677970249494836, 
            18: 0.1765375363843931, 19: 0.18422877390319162, 20: 0.19316822276007173, 
            21: 0.1996826997385783, 22: 0.21236949231329913, 23: 0.22267443097773348, 
            24: 0.23347940267290615, 25: 0.24949283896377986, 26: 0.2566876761756205, 
            27: 0.2678708269437177, 28: 0.27954119573086944, 29: 0.29034101878914165, 
            30: 0.30155808331261197, 31: 0.3117279402557108, 32: 0.32224076923625916, 
            33: 0.3331081367707903, 34: 0.344341999449342, 35: 0.3542720825792927, 
            36: 0.3644885279628326, 37: 0.3749995936718436, 38: 0.38398999457389427, 
            39: 0.39506344066320603, 40: 0.40071934468037423, 41: 0.41423335287728646, 
            42: 0.42416436072959446, 43: 0.43433345881842655, 44: 0.4447463552211064, 
            45: 0.45325613023749545, 46: 0.46412268687092223, 47: 0.4730032085410998, 
            48: 0.48205365007808243, 49: 0.4912772627279358, 50: 0.5006773599460541, 
            51: 0.5126808134549512, 52: 0.5200205801199638, 53: 0.5299706518603222, 
            54: 0.5401111082343341, 55: 0.5504455920608321, 56: 0.5583260161014446, 
            57: 0.5690090239036288, 58: 0.5771552102951079, 59: 0.5881984958251407, 
            60: 0.596619407235837, 61: 0.6080351206337894, 62: 0.616740021992414, 
            63: 0.6255695465925124, 64: 0.6345254785958663, 65: 0.6466664866145445, 
            66: 0.6559244517992534, 67: 0.6653149581332802, 68: 0.6748399031346985, 
            69: 0.684501211487295, 70: 0.6943008354294861, 71: 0.7042407551488017, 
            72: 0.7143229791820179, 73: 0.7245495448210172, 74: 0.7349225185244589, 
            75: 0.7419202059930923, 76: 0.7525418658117033, 77: 0.7633155900388464, 
            78: 0.7705836268786365, 79: 0.7853279709729015, 80: 0.7928056023731169, 
            81: 0.8041557601699713, 82: 0.815668411876591, 83: 0.823434934850752, 
            84: 0.8352235958012078, 85: 0.8471810284677068, 86: 0.8552476040823378, 
            87: 0.8674917093619414, 88: 0.8757516765159388, 89: 0.8882893272206793, 
            90: 0.9010064725120812, 91: 0.9095855560793044, 92: 0.9226075876597282, 
            93: 0.9313923498515226, 94: 0.9447265771954693, 95: 0.9537219490392906, 
            96: 0.9673758568617342, 97: 0.9765868876036025, 98: 0.99056814006128, 
            99: 0.9999999999999998}
    return dict[snapnum]
