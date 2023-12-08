# liste_pattern.py

def pattern_equivalence (): 
    liste_pattern_equivalence = [[
                    {
                        "RIGHT_ID": "anchor_founded",
                        "RIGHT_ATTRS": {'LEMMA': {"IN": ['désigner', 'désigne','signifier','représenter','être','représente','appeler',
                                                         'définir','regrouper', 'regroupe', 'englober', 'englobe','couvrir', 'inclure',
                                                         'comprendre','concerner', 'concerne','impliquer','implique','correspondre','consister','consiste',
                                                         'constitue','constituer','comporte','comporter']}}    
                    },
                    
                    {"LEFT_ID": "anchor_founded", "REL_OP": ">","RIGHT_ID": "sujet","RIGHT_ATTRS": {"DEP": "nsubj"}},
                    {"LEFT_ID": "anchor_founded","REL_OP": ">","RIGHT_ID": "objet","RIGHT_ATTRS": {"DEP": "obj"}}
                    ],
[
        {"RIGHT_ID": "verbe","RIGHT_ATTRS": {'LEMMA': {"IN": ["définir","constituer"]}}},
        {"LEFT_ID": "verbe","REL_OP": ">","RIGHT_ID": "sujet","RIGHT_ATTRS": {"DEP": "nsubj:pass"}
        },
        {"LEFT_ID": "verbe","REL_OP": ">","RIGHT_ID": "objet","RIGHT_ATTRS": {"DEP":{"IN": ['obj','obl:agent','obl:arg']}}
        }],
[
        {
            "RIGHT_ID": "verbe",
            "RIGHT_ATTRS": {'LEMMA': {"IN": ["appeler","regrouper"]}}
            
        },
        
        {"LEFT_ID": "verbe","REL_OP": ">","RIGHT_ID": "sujet","RIGHT_ATTRS": {"DEP":{"IN": ['xcomp','obj','obl:mod','obl:agent','obl:arg']}}
        },
        {"LEFT_ID": "verbe","REL_OP": ">","RIGHT_ID": "objet","RIGHT_ATTRS": {"DEP": {"IN":["nsubj:pass","nsubj"]}} #upd : ajout de nsubj
        }
    ],[
        {
            "RIGHT_ID": "verbe",
            "RIGHT_ATTRS": {'LEMMA': {"IN": ['correspondre','correspond']}}
            
        },
        {"LEFT_ID": "verbe","REL_OP": ">","RIGHT_ID": "sujet","RIGHT_ATTRS": {"DEP": "nsubj"}
        },

        {"LEFT_ID": "verbe","REL_OP": ">","RIGHT_ID": "objet","RIGHT_ATTRS": {"DEP":{"IN": ['obl:arg']}}
        }
    ],[
        {
            "RIGHT_ID": "verbe",
            "RIGHT_ATTRS": {'LEMMA': {"IN": ['faire']}}
            
        },

        {"LEFT_ID": "verbe","REL_OP": ">","RIGHT_ID": "sujet","RIGHT_ATTRS": {"DEP":{"IN": ['obl:arg']}}
        },
        {"LEFT_ID": "verbe","REL_OP": ">","RIGHT_ID": "objet","RIGHT_ATTRS": {"DEP": "nsubj"}
        },
        {"LEFT_ID": "verbe","REL_OP": ">","RIGHT_ID": "partie","RIGHT_ATTRS": {"DEP":"obj","LEMMA":"partie"}
        }
    ],[
        {
            "RIGHT_ID": "objet",
            "RIGHT_ATTRS": {"POS": "NOUN"}
            
        },
        {"LEFT_ID": "objet","REL_OP": ">","RIGHT_ID": "verbe","RIGHT_ATTRS": {"POS": "VERB","DEP":"acl:relcl"}
        },

        {"LEFT_ID": "verbe","REL_OP": ">","RIGHT_ID": "verbe_faire","RIGHT_ATTRS": {"POS":"VERB","LEMMA":"faire"}
        },
        {"LEFT_ID": "verbe_faire","REL_OP": ">","RIGHT_ID": "sujet","RIGHT_ATTRS": {"DEP":"obl:arg","POS":"NOUN"}
        },
        {"LEFT_ID": "verbe_faire","REL_OP": ">","RIGHT_ID": "partie","RIGHT_ATTRS": {"DEP":"obj","LEMMA":"partie"}
        }
    ],
[
        {
            "RIGHT_ID": "verbe",
            "RIGHT_ATTRS": {'LEMMA': {"IN": ['englober','englobe']},"DEP":"acl"}
        },

        {"LEFT_ID": "verbe","REL_OP": ">","RIGHT_ID": "sujet","RIGHT_ATTRS": {"DEP": "obj"}
        },

        {"LEFT_ID": "verbe","REL_OP": "<","RIGHT_ID": "objet","RIGHT_ATTRS": {"DEP": "nmod"}
        }
        
    ],[
        {
            "RIGHT_ID": "objet",
            "RIGHT_ATTRS": {"POS": "NOUN"}
            
        },
        {"LEFT_ID": "objet","REL_OP": ">","RIGHT_ID": "verbe","RIGHT_ATTRS": {"POS": "VERB","DEP":"acl:relcl"}
        },

        {"LEFT_ID": "verbe","REL_OP": ">","RIGHT_ID": "verbe_equi","RIGHT_ATTRS": {"POS":"VERB","LEMMA":"constituer"}
        },
        {"LEFT_ID": "verbe_equi","REL_OP": ">","RIGHT_ID": "sujet","RIGHT_ATTRS": {"DEP":"obj","POS":"NOUN"}
        }
    ],[
        {
            "RIGHT_ID": "verbe",
            "RIGHT_ATTRS": {'LEMMA': {"IN": ['consister','consiste']}}
        },
        

        {"LEFT_ID": "verbe","REL_OP": ">","RIGHT_ID": "sujet","RIGHT_ATTRS": {"DEP": "nsubj"}
        },
        {"LEFT_ID": "verbe","REL_OP": ">","RIGHT_ID": "objet","RIGHT_ATTRS": {"DEP": "xcomp"}
        }       
    ],[
        {
            "RIGHT_ID": "verbe",
            "RIGHT_ATTRS": {'LEMMA': {"IN": ["représenter","représente"]}}
            
        },
        
        {"LEFT_ID": "verbe","REL_OP": ">","RIGHT_ID": "sujet","RIGHT_ATTRS": {"DEP":"nsubj"}
        },
        {"LEFT_ID": "verbe","REL_OP": ">","RIGHT_ID": "complement","RIGHT_ATTRS": {"DEP": "obl:mod"}
        },
        {"LEFT_ID": "complement","REL_OP": ">","RIGHT_ID": "objet","RIGHT_ATTRS": {"DEP": "appos","POS":"NOUN"}
        }
    ],[
    {
        "RIGHT_ID": "anchor_founded",
        "RIGHT_ATTRS": {"LEMMA": "regrouper", "POS":"VERB"}
    },
    {"LEFT_ID": "anchor_founded","REL_OP": ">","RIGHT_ID": "objet","RIGHT_ATTRS": {"DEP": "nsubj:pass"}},
    {"LEFT_ID": "anchor_founded","REL_OP": ">","RIGHT_ID": "ce","RIGHT_ATTRS": {"DEP": "obl:mod","ORTH":"ce"}},
    {"LEFT_ID": "ce","REL_OP": ">","RIGHT_ID": "appelle","RIGHT_ATTRS": {"DEP": "acl","POS":"VERB"}},
    {"LEFT_ID": "appelle","REL_OP": ">","RIGHT_ID": "sujet","RIGHT_ATTRS": {"DEP": "xcomp"}}
    ],[
        {
            "RIGHT_ID": "objet",
            "RIGHT_ATTRS": {"POS":{"IN": ["NOUN","VERB"]}}},        
        {"LEFT_ID": "objet","REL_OP": ">","RIGHT_ID": "sujet","RIGHT_ATTRS": {"DEP": "nsubj"}},
        {"LEFT_ID": "objet","REL_OP": ">","RIGHT_ID": "verbe","RIGHT_ATTRS": {'LEMMA': {"IN": ['être']},"DEP":"cop"}} ],
        [{"RIGHT_ID": "verbe","RIGHT_ATTRS": {'LEMMA': {"IN": ["pouvoir"]}}},{"LEFT_ID": "verbe","REL_OP": ">","RIGHT_ID": "sujet","RIGHT_ATTRS": {"DEP": "nsubj"}
        },{"LEFT_ID": "verbe","REL_OP": ">","RIGHT_ID": "aux","RIGHT_ATTRS": {"DEP": "advmod","LEMMA":"être"}},
        {"LEFT_ID": "verbe","REL_OP": ">","RIGHT_ID": "objet","RIGHT_ATTRS": {"DEP":'obl:arg'}}
        ],
        [{"RIGHT_ID": "verbe","RIGHT_ATTRS": {'LEMMA': {"IN": ["pouvoir"]}}},
                        {"LEFT_ID": "verbe","REL_OP": ">","RIGHT_ID": "sujet","RIGHT_ATTRS": {"DEP": "nsubj"}},
        {"LEFT_ID": "verbe","REL_OP": ">","RIGHT_ID": "verbe2","RIGHT_ATTRS": {"DEP": "xcomp","POS":"VERB","LEMMA":"composer"}},
        {"LEFT_ID": "verbe2","REL_OP": ">","RIGHT_ID": "objet","RIGHT_ATTRS": {"DEP":'obl:arg'}
        },{"LEFT_ID": "verbe2","REL_OP": ">","RIGHT_ID": "aux","RIGHT_ATTRS": {"DEP": "aux:pass","LEMMA":"être"}
        } ]
]
    return liste_pattern_equivalence 

def pattern_possession ():
    liste_pattern_possession =[[
        {"RIGHT_ID": "anchor_founded","RIGHT_ATTRS": {'LEMMA': {"IN": ['posséder','conserver','conserve','détenir','dispose','disposer']}}},
        {"LEFT_ID": "anchor_founded","REL_OP": ">","RIGHT_ID": "objet","RIGHT_ATTRS": {"DEP": "nsubj"}},
        {"LEFT_ID": "anchor_founded","REL_OP": ">","RIGHT_ID": "que","RIGHT_ATTRS": {"LEMMA": {"IN":["que","qu'","dont"]}}},
        {"LEFT_ID": "anchor_founded","REL_OP": "<","RIGHT_ID": "sujet","RIGHT_ATTRS": {"POS": "NOUN"}}  
    ],
    [{"RIGHT_ID": "anchor_founded","RIGHT_ATTRS": {"POS": "VERB"}},
        {"LEFT_ID": "anchor_founded","REL_OP": ">","RIGHT_ID": "verbe","RIGHT_ATTRS": {'LEMMA': {"IN": ['posséder','conserver','conserve','détenir','dispose','disposer']},"DEP":"ccomp"}},
        {"LEFT_ID": "verbe","REL_OP": ">","RIGHT_ID": "objet","RIGHT_ATTRS": {"DEP": "nsubj"}},
        {"LEFT_ID": "anchor_founded","REL_OP": ">","RIGHT_ID": "sujet","RIGHT_ATTRS": {"DEP": "obl:arg"}}  
    ],
    [
        {"RIGHT_ID": "anchor_founded","RIGHT_ATTRS": {'LEMMA': {"IN": ['posséder','conserver','conserve','détenir','dispose','disposer']}}},
        {"LEFT_ID": "anchor_founded","REL_OP": ">","RIGHT_ID": "objet","RIGHT_ATTRS": {"DEP": "nsubj"}},
        {"LEFT_ID": "objet","REL_OP": ">","RIGHT_ID": "determinant","RIGHT_ATTRS": {"DEP": "det"}}, 
        {"LEFT_ID": "anchor_founded","REL_OP": "<","RIGHT_ID": "sujet","RIGHT_ATTRS": {"POS": "NOUN"}},
        {"LEFT_ID": "anchor_founded","REL_OP": ">","RIGHT_ID": "que","RIGHT_ATTRS": {"LEMMA": {"IN":["que","qu'", "dont"]}}} 
    ],
    [
        {"RIGHT_ID": "anchor_founded","RIGHT_ATTRS": {'LEMMA': {"IN": ['appartenir','posséder','conserver','conserve','détenir','disposer']},'POS': 'VERB'}},
        {"LEFT_ID": "anchor_founded","REL_OP": "<","RIGHT_ID": "sujet","RIGHT_ATTRS": {"POS": {"IN": ["NOUN","ADJ"]}}}, #ajout adj
        {"LEFT_ID": "anchor_founded","REL_OP": ">","RIGHT_ID": "objet","RIGHT_ATTRS": {"POS": {"IN": ["NOUN"]}}} 
    ],
    [
        {"RIGHT_ID": "anchor_founded","RIGHT_ATTRS": {'LEMMA': {"IN": ['posséder','conserver','conserve','détenir','disposer']},'POS': 'VERB'}},
        {"LEFT_ID": "anchor_founded","REL_OP": ">","RIGHT_ID": "sujet","RIGHT_ATTRS": {"DEP": {"IN": ["nsubj"]}}}, #avant POS : NOUN
        {"LEFT_ID": "anchor_founded","REL_OP": ">","RIGHT_ID": "objet","RIGHT_ATTRS": {"DEP": {"IN": ["obj"]}}},
        
    ],
    [
        {"RIGHT_ID": "sujet","RIGHT_ATTRS": {'POS': 'NOUN'}},
        {"LEFT_ID": "sujet","REL_OP": ">","RIGHT_ID": "verbe","RIGHT_ATTRS":  {'LEMMA': {"IN": ['posséder','conserver','conserve','détenir','disposer','appartenir']},'POS': 'VERB','dep': 'acl'}},
        {"LEFT_ID": "verbe","REL_OP": ">","RIGHT_ID": "objet","RIGHT_ATTRS": {"POS": 'NOUN'}},
        {"LEFT_ID": "objet","REL_OP": ">","RIGHT_ID": "par","RIGHT_ATTRS": {"dep": 'case'}},
        
    ],
    [
        {"RIGHT_ID": "anchor_verb","RIGHT_ATTRS": {'LEMMA': 'détenteur'}},
        {"LEFT_ID": "anchor_verb","REL_OP": ">","RIGHT_ID": "objet","RIGHT_ATTRS": {"dep": 'nsubj'}},
        {"LEFT_ID": "anchor_verb","REL_OP": ">","RIGHT_ID": "sujet","RIGHT_ATTRS": {"dep": 'nmod',"POS":"NOUN"}},
        
    ]

    ]
    return liste_pattern_possession 

def pattern_but():
    liste_pattern_but =[
         [{"RIGHT_ID": "anchor_verb","RIGHT_ATTRS": {'LEMMA': {"IN": ['vise','viser', 'servir','destiner','prêt',"œuvre","œuvrer"]}}},
          {"LEFT_ID": "anchor_verb","REL_OP": ">","RIGHT_ID": "but","RIGHT_ATTRS": {"DEP": {"IN": ["xcomp","obl:arg"]}}}],

          [{"RIGHT_ID": "anchor_verb","RIGHT_ATTRS": {'LEMMA': 'permettre'}},
           {"LEFT_ID": "anchor_verb","REL_OP": ">","RIGHT_ID": "but","RIGHT_ATTRS": {"DEP": {"IN":["xcomp","obl:arg"]}}}], #up obl:arg
           
        [{"RIGHT_ID": "anchor_verb","RIGHT_ATTRS": {"DEP": {"IN": ["acl", "advcl",]}}}, #ajoutnmod
        {"LEFT_ID": "anchor_verb","REL_OP": ">","RIGHT_ID": "but","RIGHT_ATTRS": {"POS": "ADP","LEMMA":"pour"}}],
        
        [{"RIGHT_ID": "anchor_verb","RIGHT_ATTRS": {"DEP": {"IN":["obl:mod","obl:arg"]}, "ORTH":"vue"}},
         {"LEFT_ID": "anchor_verb","REL_OP": ">","RIGHT_ID": "but","RIGHT_ATTRS": {"POS": "ADP"}}],
        
        [{"RIGHT_ID": "anchor_verb","RIGHT_ATTRS" :{'ORTH': {"IN":["attendant","prévision","attente","préparation","permettant"]}}}, #up permettant
         {"LEFT_ID": "anchor_verb","REL_OP": ">","RIGHT_ID": "but","RIGHT_ATTRS": {"DEP": {"IN":["xcomp","case","obj"]}}}], #up obj

        [{"RIGHT_ID": "anchor_verb","RIGHT_ATTRS": {'LEMMA': 'permettre'}},
           {"LEFT_ID": "anchor_verb","REL_OP": ">","RIGHT_ID": "sujet","RIGHT_ATTRS": {"DEP": "obl:arg"}},
           {"LEFT_ID": "sujet","REL_OP": ">","RIGHT_ID": "but","RIGHT_ATTRS": {"DEP": "acl"}}] #permettre à [sujet] de [objet]
    ]
    return(liste_pattern_but) 

def pattern_obligation():
    liste_pattern_obligation = [[
    {"RIGHT_ID": "anchor_founded","RIGHT_ATTRS": {"LEMMA": "engager", "POS":"VERB"}},
    {"LEFT_ID": "anchor_founded","REL_OP": ">","RIGHT_ID": "sujet","RIGHT_ATTRS": {"DEP": "nsubj"}},
    {"LEFT_ID": "anchor_founded","REL_OP": ">","RIGHT_ID": "objet","RIGHT_ATTRS": {"DEP": "xcomp"}}
   ],
   [
    {"RIGHT_ID": "sujet","RIGHT_ATTRS": { "POS":"NOUN"}},
    {"LEFT_ID": "sujet","REL_OP": ">","RIGHT_ID": "necessaire","RIGHT_ATTRS": {"LEMMA": "nécessaire","DEP":"amod"}},
    {"LEFT_ID": "necessaire","REL_OP": ">","RIGHT_ID": "objet","RIGHT_ATTRS": {"DEP": "obl:arg"}},
    {"LEFT_ID": "objet","REL_OP": ">","RIGHT_ID": "a","RIGHT_ATTRS": {"DEP": "case","POS":"ADP"}}
   ],
   [
    {"RIGHT_ID": "anchor_founded","RIGHT_ATTRS": {"LEMMA":"nécessaire"}},
    {"LEFT_ID": "anchor_founded","REL_OP": ">","RIGHT_ID": "sujet","RIGHT_ATTRS": {"DEP": "nsubj"}},
    {"LEFT_ID": "anchor_founded","REL_OP": ">","RIGHT_ID": "objet","RIGHT_ATTRS": {"DEP": "advcl"}},
    {"LEFT_ID": "objet","REL_OP": ">","RIGHT_ID": "pour","RIGHT_ATTRS": {"DEP": "mark","POS":"ADP","LEMMA":"pour"}}
   ],
   [
    {"RIGHT_ID": "anchor_founded","RIGHT_ATTRS": {"LEMMA":"devoir"}},
    {"LEFT_ID": "anchor_founded","REL_OP": ">","RIGHT_ID": "sujet","RIGHT_ATTRS": {"DEP": "nsubj"}},
    {"LEFT_ID": "anchor_founded","REL_OP": ">","RIGHT_ID": "objet","RIGHT_ATTRS": {"DEP": "xcomp"}}
   ],
   [
    {"RIGHT_ID": "anchor_founded","RIGHT_ATTRS": { "POS":"VERB"}},
    {"LEFT_ID": "anchor_founded","REL_OP": ">","RIGHT_ID": "objet","RIGHT_ATTRS": {"DEP": "obj"}},
    {"LEFT_ID": "anchor_founded","REL_OP": ">","RIGHT_ID": "pour","RIGHT_ATTRS": {"DEP": "mark","POS":"ADP","LEMMA":"pour"}}
   ],
   [
    {"RIGHT_ID": "anchor_founded","RIGHT_ATTRS": {"POS":"NOUN"}},
    {"LEFT_ID": "anchor_founded","REL_OP": ">","RIGHT_ID": "necessaire","RIGHT_ATTRS": {"DEP": "amod","POS":"ADJ","LEMMA":"nécessaire"}}
    ],
    [
    {"RIGHT_ID": "nom","RIGHT_ATTRS": {"POS":"NOUN"}},
    {"LEFT_ID": "nom","REL_OP": ">","RIGHT_ID": "anchor_founded","RIGHT_ATTRS": {"LEMMA":"devoir","DEP":"ccomp"}},
    
    {"LEFT_ID": "anchor_founded","REL_OP": ">","RIGHT_ID": "sujet","RIGHT_ATTRS": {"DEP": "nsubj"}},
    {"LEFT_ID": "anchor_founded","REL_OP": ">","RIGHT_ID": "objet","RIGHT_ATTRS": {"DEP": "xcomp"}},
    {"LEFT_ID": "objet","REL_OP": ">","RIGHT_ID": "verbe","RIGHT_ATTRS": {"DEP": "advcl"}},
    {"LEFT_ID": "verbe","REL_OP": ">","RIGHT_ID": "fin_verbe","RIGHT_ATTRS": {"DEP": "obj"}},
    {"LEFT_ID": "verbe","REL_OP": ">","RIGHT_ID": "pour","RIGHT_ATTRS": {"DEP": "mark","POS":"ADP"}}
   ],
   [{"RIGHT_ID": "anchor_founded","RIGHT_ATTRS": {"LEMMA":{"IN": ['obligation','impératif']}}},
    {"LEFT_ID": "anchor_founded","REL_OP": ">","RIGHT_ID": "sujet","RIGHT_ATTRS": {"DEP": "nsubj"}},
    {"LEFT_ID": "anchor_founded","REL_OP": ">","RIGHT_ID": "objet","RIGHT_ATTRS": {"LEMMA": "être","DEP":"cop"}}
   ],
   [{"RIGHT_ID": "anchor_founded","RIGHT_ATTRS": {"LEMMA":"répondre"}},
    {"LEFT_ID": "anchor_founded","REL_OP": ">","RIGHT_ID": "sujet","RIGHT_ATTRS": {"DEP": "nsubj"}},
    {"LEFT_ID": "anchor_founded","REL_OP": ">","RIGHT_ID": "objet","RIGHT_ATTRS": {"DEP":"obl:arg"}}
   ]
   ]
    return liste_pattern_obligation

def pattern_contrepartie(): 
    liste =[]
    return(liste)