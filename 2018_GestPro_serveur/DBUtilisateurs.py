import sqlite3



class DbUtilisateurs:
	def __init__(self):
		self.conn = sqlite3.connect("inscription.bd")
		self.c = self.conn.cursor()
		self.creationInscription()
		self.creationProjet()
		self.creationUserProjet()
		self.creationChat()
		self.creationMandat()
		self.creationAnalyseTextuelle()
		self.creationLigneCasUsage()
		self.creationScenario()
		self.creationCasUsage()
		self.creationCRC()
		self.creationBlocTemps()
		self.creationModelisation()
		self.creationplanif()

	def creationInscription(self):
		self.c.execute(''' CREATE TABLE IF NOT EXISTS utilisateurs(
				id				INTEGER		PRIMARY KEY AUTOINCREMENT,
				identifiant		TEXT		NOT NULL,
				courriel		TEXT		NOT NULL,
				statut_conf		INTEGER		DEFAULT 0,
				mot_de_passe	TEXT		NOT NULL,
				type_acces		INTEGER		DEFAULT 1,
				question_sec	TEXT		NOT NULL,
				reponse_ques 	TEXT		NOT NULL,

				CONSTRAINT uc_user_courriel		UNIQUE(courriel),
				CONSTRAINT uc_user_identifiant	UNIQUE(identifiant)
														) ''') 
		
	def creationModelisation(self):
		self.c.execute(''' CREATE TABLE IF NOT EXISTS modelisation(
				id				INTEGER		PRIMARY KEY AUTOINCREMENT,
				id_projet		INTEGER		NOT NULL,
				texte_table		TEXT		NOT NULL,
				nom_table		TEXT		NOT NULL,

				CONSTRAINT uc_id_projet		UNIQUE(id_projet, nom_table)
														) ''')
	
	
	def creationProjet(self):
		self.c.execute(''' CREATE TABLE IF NOT EXISTS projet(
				id				INTEGER		PRIMARY KEY AUTOINCREMENT,
				nom				TEXT		NOT NULL,
				id_createur		INTEGER		NOT NULL,
				description 	TEXT,
				nom_organi		TEXT,
				date_creation	TEXT		NOT NULL,
				date_butoire	TEXT,

				CONSTRAINT uc_createur_nom UNIQUE(nom,id_createur),
				CONSTRAINT fk_pro_id_createur FOREIGN KEY (id_createur) REFERENCES utilisateurs(id)

														) ''') 
	def creationUserProjet(self):
		self.c.execute(''' CREATE TABLE IF NOT EXISTS user_projet(
				id_user			INTEGER		NOT NULL,
				id_projet		INTEGER		NOT NULL,		

				CONSTRAINT pk_user_projet PRIMARY KEY(id_user,id_projet),
				CONSTRAINT fk_userPro_iduser FOREIGN KEY (id_user) REFERENCES utilisateurs(id),
				CONSTRAINT fk_userPro_idpro FOREIGN KEY (id_projet) REFERENCES projet(id)
														) ''')
	
	def creationChat(self):
		self.c.execute(''' CREATE TABLE IF NOT EXISTS chat(
				id				INTEGER		PRIMARY KEY AUTOINCREMENT,					
				identifiant		TEXT		NOT NULL,
				id_projet		INTEGER		NOT NULL,		
				message			TEXT		NOT NULL,
				time			TEXT		NOT NULL,

				CONSTRAINT fk_userPro_idpro FOREIGN KEY (id_projet) REFERENCES projet(id)
														) ''')
		
	def creationMandat(self):
		self.c.execute(''' CREATE TABLE IF NOT EXISTS mandat(
				id				INTEGER		PRIMARY KEY AUTOINCREMENT,
				fichier_txt		TEXT		NOT NULL,
				id_projet		INTEGER		NOT NULL,

				CONSTRAINT fk_mandat_projet	FOREIGN KEY (id_projet) REFERENCES projet(id)
														) ''')
		
	def creationAnalyseTextuelle(self):
		self.c.execute(''' CREATE TABLE IF NOT EXISTS analyse(
				id				INTEGER		PRIMARY KEY AUTOINCREMENT,
				id_projet		INTEGER		NOT NULL,
				fichierMandat 	TEXT,
				fichNomExp		TEXT,
				fichVerbeExp	TEXT,
				fichAdjExp		TEXT,
				fichNomImp		TEXT,
				fichVerbeImp	TEXT,
				fichAdjImp		TEXT,
				fichNomSupp		TEXT,
				fichVerbeSupp	TEXT,
				fichAdjSupp		TEXT,
				
				CONSTRAINT fk_analyse_projet	FOREIGN KEY (id_projet) REFERENCES projet(id)
														) ''')	
	
	def creationBlocTemps(self):
		self.c.execute(''' CREATE TABLE IF NOT EXISTS bloc_temps(
				id				INTEGER		PRIMARY KEY AUTOINCREMENT,
				id_projet		INTEGER		NOT NULL,
				debut			DATE		NOT NULL,
				fin				DATE		NOT NULL,

				CONSTRAINT fk_bloc_projet	FOREIGN KEY (id_projet) REFERENCES projet(id)
														) ''')
		
	def creationScenario(self):
		self.c.execute('''CREATE TABLE IF NOT EXISTS scenario(
				id                    INTEGER        PRIMARY KEY AUTOINCREMENT,
                id_projet             INTEGER         NOT NULL,
                id_cas                INTEGER         NOT NULL,
                utilisateur           TEXT            NOT NULL,
                ordinateur            TEXT            NOT NULL,
                autre                 TEXT            NOT NULL,
               
                	CONSTRAINT fk_sceanrio_projet    FOREIGN KEY (id_projet) REFERENCES projet(id)
                	CONSTRAINT fk_scenario_cas       FOREIGN KEY (id_cas) REFERENCES cas_usage(id)
														) ''')
	

	def creationCasUsage(self):
		self.c.execute('''CREATE TABLE IF NOT EXISTS cas_usage(
				id                    INTEGER        PRIMARY KEY AUTOINCREMENT,
                id_projet             INTEGER        NOT NULL,
                description           TEXT           NOT NULL,
            
                CONSTRAINT fk_sceanrio_projet    FOREIGN KEY (id_projet) REFERENCES projet(id)
														) ''')			
				
	def creationLigneCasUsage(self):
		self.c.execute('''CREATE TABLE IF NOT EXISTS ligne_cas(
				id                        INTEGER        PRIMARY KEY AUTOINCREMENT,
                id_cas                    INTEGER,
                type                      TEXT,
                description               TEXT,
                
                CONSTRAINT fk_ligne                FOREIGN KEY (id_cas) REFERENCES cas_usage(id)
														) ''')
		
				
	def creationCRC(self):
		self.c.execute('''CREATE TABLE IF NOT EXISTS crc(	
				id				INTEGER		PRIMARY KEY AUTOINCREMENT,
				id_projet		INTEGER		NOT NULL,
				id_fiche		INTEGER         NOT NULL,
				classe                  TEXT            NOT NULL,
				proprietaire            TEXT,
                                collaboration           TEXT,
                                responsabilites         TEXT,
                                parametres               TEXT,
				
				CONSTRAINT fk_crc_projet	FOREIGN KEY (id_projet) REFERENCES projet(id)				
														) ''')
			###CONSTRAINT fk_crc_utilisateur	FOREIGN KEY (id_utilisateur) REFERENCES utilisateurs(id)
				
	def creationplanif(self):
		self.c.execute('''CREATE TABLE IF NOT EXISTS planif(	
				id				INTEGER			PRIMARY KEY AUTOINCREMENT,
				id_projet		INTEGER			NOT NULL,
				nom		   		INTEGER         NOT NULL,
								
				CONSTRAINT fk_crc_projet	FOREIGN KEY (id_projet) REFERENCES projet(id)				
														) ''') 			
				

				
