from funciones import *
import os
import pandas as pd
import numpy as np



r_directorios = "c:/Users/brial/OneDrive - dane.gov.co/Cruce de directorios-Transporte"

sub_carpetas = {}

if os.path.exists(r_directorios) and os.path.isdir(r_directorios):

    for subcarpeta in os.listdir(r_directorios):
        r_subcarpeta = os.path.join(r_directorios, subcarpeta)

        if os.path.isdir(r_subcarpeta):
            archivos = os.listdir(r_subcarpeta)
            archivos = [f for f in archivos if os.path.isfile(os.path.join(r_subcarpeta, f))]
            sub_carpetas[subcarpeta] = archivos
else:
    print(f"La ruta {r_directorios} no existe o no es una carpeta válida.")

sub_carp_xlsx = {}

for carpeta, archivos in sub_carpetas.items():
    archivos_xlsx = [archivo for archivo in archivos if isinstance(archivo, str) and archivo.endswith('.xlsx')]
    if archivos_xlsx:
        sub_carp_xlsx[carpeta] = archivos_xlsx

n_directorios = list(sub_carpetas.keys())

ruta_archivo = os.path.join(r_directorios, n_directorios[0], sub_carp_xlsx['DIG'][0])

##______________________________________________________________
###_______________________ Objetivo ____________________________

r_obj = os.path.join(r_directorios,"Consolidad_directorio.xlsx")
df_obj = pd.read_excel(r_obj, sheet_name = 'CENU-ENTREGA', 
                        decimal = ',')

names_obj = list(df_obj.columns)

##______________________________________________________________
###_______________________ FEST ________________________________

r_fest = os.path.join(r_directorios,"20240527_Directorio_Transporte - fest.xlsx")

df_fest = pd.read_excel(r_fest, sheet_name = 'CENU-ENTREGA', 
                        decimal = ',')

df_fest_f = df_estandar(df_fest, names_obj)

df_fest_f[names_obj[27]] = 'si'

##______________________________________________________________
###_______________________ DIG ________________________________

r_DIG = os.path.join(r_directorios, 
                        n_directorios[0], 
                        sub_carpetas[n_directorios[0]][3])

df_DIG = pd.read_excel(r_DIG, sheet_name= 0, 
                          decimal = ',')

indic = {0:4, 1:5, 2:7, 3:8, 4:15, 6:0, 7:2, 8:13, 9:14, 11:17, 12:16,
13:9, 14:10, 15:11, 16:12, 17:26, 18:23, 20:25}

df_consol = cruce(df_fest_f, df_DIG, names_obj, indic, sub_carpetas[n_directorios[0]][3])

##______________________________________________________________
###______________________ DIMAR ________________________________

r_DIMAR = os.path.join(r_directorios, 
                        n_directorios[1], 
                        sub_carpetas[n_directorios[1]][1])

df_DIMAR = pd.read_excel(r_DIMAR, sheet_name= 0, 
                          decimal = ',')

indic = {0:5, 2:7, 3:2, 4:3, 5:1, 6:0, 7:15, 8:13, 9:17, 10:16}

df_consol = cruce(df_consol, df_DIMAR, names_obj, indic, sub_carpetas[n_directorios[1]][1])

##______________________________________________________________
###_______________________ ETUPa _______________________________

r_ETUPa = os.path.join(r_directorios, 
                        n_directorios[2], 
                        sub_carpetas[n_directorios[2]][0])

df_ETUPa = pd.read_excel(r_ETUPa, sheet_name= 0, 
                          decimal = ',')

indic = {2:3, 3:1, 4:5, 5:6, 6:7, 7:15, 8:16, 9:13, 10:17, 13:14}

df_consol = cruce(df_consol, df_ETUPa, names_obj, indic, sub_carpetas[n_directorios[2]][0])

##______________________________________________________________
###_______________________ ETUPb _______________________________

r_ETUPb = os.path.join(r_directorios, 
                        n_directorios[2], 
                        sub_carpetas[n_directorios[2]][4])

df_ETUPb = pd.read_excel(r_ETUPb, sheet_name= 0, 
                          decimal = ',')

indic = {1:5, 2:7, 3:21, 6:3, 7:15, 8:13, 9:17, 12:9}

df_consol = cruce(df_consol, df_ETUPb, names_obj, indic, sub_carpetas[n_directorios[2]][4])

##______________________________________________________________
###_______________________ MINTRANS ____________________________
#_________________________ RNDC ________________________________

r_MINTRANSa = os.path.join(r_directorios, 
                        n_directorios[3], 
                        sub_carpetas[n_directorios[3]][0])

df_MINTRANSa = pd.read_excel(r_MINTRANSa, sheet_name= 0, 
                          decimal = ',')

indic = {0:7, 1:5, 3:15, 4:3, 5:13, 6:17}

df_consol = cruce(df_consol, df_MINTRANSa, names_obj, indic, sub_carpetas[n_directorios[3]][0])

##______________________________________________________________
###_______________________ MINTRANS ____________________________
#___________________________ RUNT ______________________________

r_MINTRANSb = os.path.join(r_directorios, 
                        n_directorios[3], 
                        sub_carpetas[n_directorios[3]][2])

df_MINTRANSb = pd.read_excel(r_MINTRANSb, sheet_name= 0, 
                          decimal = ',')

indic = {0:5, 1:7, 2:13, 3:15, 4:3, 6:17}

df_consol = cruce(df_consol, df_MINTRANSb, names_obj, indic, sub_carpetas[n_directorios[3]][2])

##______________________________________________________________
###_______________________ MINTRANS ____________________________
#_________________________ TTCARGA _____________________________

r_MINTRANSc = os.path.join(r_directorios, 
                        n_directorios[3], 
                        sub_carpetas[n_directorios[3]][3])

df_MINTRANSc = pd.read_excel(r_MINTRANSc, sheet_name= None, 
                          decimal = ',')

df_MINTRANSc = pd.concat(df_MINTRANSc.values(), ignore_index=True)

indic = {0:7, 1:5, 3:15, 4:3, 5:13, 6:17}

df_consol = cruce(df_consol, df_MINTRANSc, names_obj, indic, sub_carpetas[n_directorios[3]][3])

##______________________________________________________________
###____________________ SuperTransporte ________________________
#______________________ SuperTransporte ________________________

r_supert = os.path.join(r_directorios, 
                        n_directorios[5], 
                        sub_carp_xlsx[n_directorios[5]][0])
df_supert = pd.read_excel(r_supert, sheet_name= 'EMPRESAS TIP', 
                          decimal = ',')

indic = {8:1, 0:5, 1:7, 2:8, 5:13, 10:15, 9:16, 7:17}

df_consol = cruce(df_consol, df_supert, names_obj, indic, sub_carpetas[n_directorios[5]][0])

##______________________________________________________________
###______________________ Transporte ___________________________
#________________________ Transporte ___________________________

r_TRANS = os.path.join(r_directorios, 
                        n_directorios[6], 
                        sub_carpetas[n_directorios[6]][2])

df_TRANS = pd.read_excel(r_TRANS, sheet_name= 0, 
                          decimal = ',')

indic = {2:0, 3:1, 4:2, 5:3, 6:4, 7:5, 8:6, 
         9:7, 10:8, 12:9, 14:13, 15:14, 16:15, 
         17:16, 18:17, 19:19, 24:20, 25:21, 27:22, 
         28:23}

df_consol = cruce(df_consol, df_TRANS, names_obj, indic, sub_carpetas[n_directorios[6]][2])

df_consol.to_excel('Consolidado_directorios.xlsx', index = False)




##______________________________________________________________
###__________________ Listado de duplicados ____________________
#____________________ Listado de duplicados ____________________


directorios = [df_DIG, df_DIMAR, df_ETUPa, df_ETUPb, df_MINTRANSa, 
               df_MINTRANSb,df_MINTRANSc, df_supert, df_TRANS]

xlsx_directorios = [n_directorios[0] + "-" +  sub_carpetas[n_directorios[0]][3],
                     n_directorios[1] + "-" +  sub_carpetas[n_directorios[1]][1],
                         n_directorios[2] + "-" +  sub_carpetas[n_directorios[2]][0],
                             n_directorios[2] + "-" +  sub_carpetas[n_directorios[2]][4],
                                 n_directorios[3] + "-" +  sub_carpetas[n_directorios[3]][0],
                                     n_directorios[3] + "-" +  sub_carpetas[n_directorios[3]][2],
                                         n_directorios[3] + "-" +  sub_carpetas[n_directorios[3]][3],
                                             n_directorios[5] + "-" +  sub_carpetas[n_directorios[5]][0],
                                                 n_directorios[6] + "-" +  sub_carpetas[n_directorios[6]][2]]

ind_nit = [1, 0, 4, 1, 1, 0, 1, 0, 7]

dup_list = []

for i in range(9):

    df_dup = directorios[i][directorios[i].duplicated(subset = 
                                             directorios[i].columns[ind_nit[i]], keep=False)]
    df_dup = df_dup[[directorios[i].columns[ind_nit[i]]]]

    df_dup['Origen'] = xlsx_directorios[i]
    
    df_dup = df_dup.rename(columns = {df_dup.columns[0]: "Nit"})

    dup_list.append(df_dup)

dup_list_f = [df for df in dup_list if not df.empty]

df_dup_f = pd.concat(dup_list_f, ignore_index=True)


df_dup_f.to_excel('Listado de nit de duplicados.xlsx', index=False)

df_informe = pd.DataFrame(xlsx_directorios, columns=['Directorio'])
df_informe['Cantidad de empresas'] = None
df_informe['Cantidad que coincide con Fest'] = None
df_informe['Cantidad que no coincide con Fest'] = None

for i in range(9):
    df_informe.iloc[i,1] = directorios[i].shape[0]
    df_informe.iloc[i,2] = directorios[i][directorios[i].columns[ind_nit[i]]].isin(df_fest_f[names_obj[5]]).sum()
    df_informe.iloc[i,3] = df_informe.iloc[i,1] - df_informe.iloc[i,2]

df_informe.to_excel('Informe Empresas respecto a Fest.xlsx', index=False)

df_informe2 = pd.DataFrame(xlsx_directorios.append(df_fest_f), columns=['Directorio'])
df_informe2['Cantidad de empresas'] = None
df_informe2['Cantidad que coincide con DIG'] = None
df_informe2['Cantidad que no coincide con DIG'] = None

for i in range(9):
    df_informe2.iloc[i,1] = directorios[i].shape[0]
    df_informe2.iloc[i,2] = directorios[i][directorios[i].columns[ind_nit[i]]].isin(df_DIG[df_DIG.columns[1]]).sum()
    df_informe2.iloc[i,3] = df_informe2.iloc[i,1] - df_informe2.iloc[i,2]

df_informe2.to_excel('Informe Empresas respecto a DIG.xlsx', index=False)


df_consoli = df_consol.copy()

df_consoli[names_obj[26]] = df_consoli.apply(lambda row: 
                                 ocupados(row,df_DIG), axis = 1)

df_consoli.to_excel('Consolidado_directorios.xlsx', index=False)
