# extract_sequences (ExSeq)
Python code to extract sequences from sequencing (e.g. fasta/bisulfite) files.

---

# Getting Started
In order to download `ExSeq`, you should clone this repository via the commands
```  
git clone https://github.com/MischaLundberg/extract_sequences
cd extract_sequences
```

In order to install the Python dependencies, you will need the [Anaconda](https://store.continuum.io/cshop/anaconda/) Python distribution and package manager. After installing Anaconda, run the following commands to create an environment with ExSeq's dependencies:

```
conda env create --file environment.yml
conda activate ExSeq

## to deactivate the environment, type
#conda deactivate
```

In case you are updating your current version of ExSeq, it would be best practice to also update your environment to the updated prerequisetes.
If you are using a Anaconda environment, you can do so by typing
```
conda env update --name ExSeq --file environment.yml
```


If you receive any errors while running ExSeq, please ensure your versioning for the prerequisites is according to the tested versions.

---

# Input

```
usage: ExSeq.py [-h] -i INPUT [--raadIdentifier READIDENTIFIER] --nReads NREADS [--firstRead FIRSTREAD] --output OUTPUT
```

Extracting sequences from sequencing files (e.g. fasta/bisulfite).

:information_source: Please remember, if you are not natively using Python 3 to load the environment ```conda activate CpGmeth```

You can start a run like: 
```
/DIRECTORY/ExSeq.py -i /FILE_DIRECTORY/simplebs_480.sorted_CpG.bedGraph -r /FILE_DIRECTORY/L1HS.rmsk.txt -o /FILE_DIRECTORY/simplebs_480.bedGraph
```

If you want to start your run with *FASTQ* files, your arguments should be set as following:
```
/DIRECTORY/CpG_Meth.py -i /FILE_DIRECTORY/simplebs_480.1.fastq -n 5 -o /FILE_DIRECTORY/simplebs_480.1.1-5.fastq 
```
---

# Further development
Please contact me for future developments.
---

# Contact
For questions or errors, either create a issue/pullrequest or contact me via email (mischa(dot)lundberg(at)regionh(dot)dk

---

# Dont forget to cite
