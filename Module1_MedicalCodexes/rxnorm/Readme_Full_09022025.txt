September 02, 2025

README: RxNorm 09/02/2025 Full Update Release
===================================================

-----------------------------------------------------------------
This Full release contains data that is consistent with the
2020AA version of the UMLS.
-----------------------------------------------------------------
This release contains updates to the following sources:

ATC -  2025_02_10 (Anatomical Therapeutic Chemical Classification System)
GS -  08/11/2025 (Gold Standard Alchemy)
CVX -  08/15/2025 (Vaccines Administered,  2025_08_15)
MMSL -  08/01/2025 (Multum MediSource Lexicon)
MMX -  08/01/2025 (Micromedex DRUGDEX)
MTHSPL -  08/23/2025 (FDA Structured Product Labels)
NDDF -  08/13/2025 (First Databank FDB MedKnowledge (formerly NDDF Plus))
#NDFRT -  (National Drug File - Reference Terminology)
VANDF -  07/31/2025 (Veterans Health Administration National Drug File)
DRUGBANK -  08/13/2025 (DrugBank,  5.0_2025_08_13)
USP -  01/30/2025 (USP Compendial Nomenclature)

For full details, please refer to the RxNorm documentation at
https://www.nlm.nih.gov/research/umls/rxnorm/docs/index.html.

This release contains database control files and SQL
commands for use in the automation of the loading process of
these files into an Oracle RDBMS.In addition, scripts are now
provided for loading the RxNorm files into a MySQL database.

RxNorm release data files are available by download from
the NLM download server at:

        https://www.nlm.nih.gov/research/umls/rxnorm/docs/rxnormfiles.html

This link will take you to a page for downloading the latest files:
RxNorm_full_09022025.zip
Once downloaded, it must be unzipped in order to access the files.

HARDWARE AND SOFTWARE RECOMMENDATIONS
-------------------------------------
- Supported operating systems:
        Windows: 7
        Linux
        Solaris: Solaris 10

- Hardware Requirements

  - A MINIMUM 2.01 GB of free hard disk space (To accomodate ZIP files and
        unzipped contents).

CONTENTS OF THE ZIP FILE
-------------------------

The ZIP formatted file is 254,515,214 bytes and contains the
following 44 files and 9 directories:

Readme_Full_09022025.txt            5480                 bytes

rrf directory:

RXNATOMARCHIVE.RRF                  81,399,045           bytes
RXNCONSO.RRF                        129,187,149          bytes
RXNCUICHANGES.RRF                   17,525               bytes
RXNCUI.RRF                          1,745,215            bytes
RXNDOC.RRF                          219,293              bytes
RXNREL.RRF                          515,672,939          bytes
RXNSAB.RRF                          10,085               bytes
RXNSAT.RRF                          544,898,285          bytes
RXNSTY.RRF                          19,956,591           bytes


scripts directory:

        oracle sub-directory:

populate_oracle_rxn_db.bat          1,164                bytes
RXNATOMARCHIVE.ctl                  564                  bytes
RXNCONSO.ctl                        512                  bytes
RXNCUICHANGES.ctl                   346                  bytes
RXNCUI.ctl                          296                  bytes
RXNDOC.ctl                          248                  bytes
rxn_index.sql                       660                  bytes
RxNormDDL.sql                       3,291                bytes
RXNREL.ctl                          471                  bytes
RXNSAB.ctl                          674                  bytes
RXNSAT.ctl                          378                  bytes
RXNSTY.ctl                          267                  bytes

         mysql sub-directory:

Indexes_mysql_rxn.sql               662                  bytes
Load_scripts_mysql_rxn_unix.sql     3,961                bytes
Load_scripts_mysql_rxn_win.sql      3,959                bytes
Populate_mysql_rxn.bat              775                  bytes
populate_mysql_rxn.sh               1,609                bytes
Table_scripts_mysql_rxn.sql         4,205                bytes

prescribe directory:

Readme_Full_Prescribe_09022025.txt  3077                 bytes

      rrf sub-directory:

RXNCONSO.RRF                        30,317,152           bytes
RXNREL.RRF                          193,919,893          bytes
RXNSAT.RRF                          274,089,764          bytes


      scripts sub-directory:

         oracle sub-directory:

populate_oracle_rxn_db.bat          699                  bytes
RXNCONSO.ctl                        512                  bytes
rxn_index.sql                       460                  bytes
RxNormDDL.sql                       1,373                bytes
RXNREL.ctl                          471                  bytes
RXNSAT.ctl                          378                  bytes

         mysql sub-directory:

Indexes_mysql_rxn.sql               463                  bytes
Load_scripts_mysql_rxn_unix.sql     1,469                bytes
Load_scripts_mysql_rxn_win.sql      1,468                bytes
Populate_mysql_rxn.bat              777                  bytes
populate_mysql_rxn.sh               1,609                bytes
Table_scripts_mysql_rxn.sql         1,749                bytes
Additional NOTES:

-----------------

- Most RxNorm users will need applications and data management
  systems such as an RDBMS for storage and retrieval.

- The RxNorm release files contain UTF-8 Unicode encoded data.

- Refer to the RxNorm release documentation at
  https://www.nlm.nih.gov/research/umls/rxnorm/docs/index.html
