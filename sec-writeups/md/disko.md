# DISKO 1,2,3

---

this is a [pico ctf](https://picoctf.org/) challenge

---

#### Disko 1

##### Description
> Can you find the flag in this disk image?

First thing I did was do `file disko-1.dd.gz` this gives me an idea of what I'm working with:
```
disko-1.dd.gz: gzip compressed data
was "disko-1.dd", last modified: Thu May 15 18:48:20 2025,
from Unix, original size modulo 2^32 52428800
```
This is a gunzip compressed file so I unzipped it with gunzip `gunzip disko-1.dd.gz`
then checked the file info agin `file disk-1.dd`
```
disko-1.dd: DOS/MBR boot sector, code offset 0x58+2,
OEM-ID "mkfs.fat", Media descriptor 0xf8, sectors/track 32,
heads 8, sectors 102400 (volumes > 32 MB), FAT (32 bit),
sectors/FAT 788, serial number 0x241a4420, unlabeled
```
When I looked inside the contents of the file it looked like it had some comprehensible text.
So I used the strings program and pipped that into grep to check for any strings with the word `pico` in the string:
```
$ strings disko-1.dd | grep "pico"

:/icons/appicon
# $Id: piconv,v 2.8 2016/08/04 03:15:58 dankogai Exp $
piconv -- iconv(1), reinvented in perl
  piconv [-f from_encoding] [-t to_encoding]
  piconv -l
  piconv -r encoding_alias
  piconv -h
B<piconv> is perl version of B<iconv>, a character encoding converter
a technology demonstrator for Perl 5.8.0, but you can use piconv in the
piconv converts the character encoding of either STDIN or files
Therefore, when both -f and -t are omitted, B<piconv> just acts
picoCTF{1t5_ju5t_4_5tr1n9_be6031da}
```
The flag printed right out of the command `picoCTF{1t5_ju5t_4_5tr1n9_be6031da}` was the correct flag.


#### Disko 2

##### Description
> Can you find the flag in this disk image? The right one is Linux! One wrong step and its all gone! 

Okay so I did the same commands as last. I got to the Strings section and It returned loads of flags:
```
picoCTF{4_P4Rt_1t_i5_c03b93aa}
picoCTF{4_P4Rt_1t_i5_aa9cb033}
picoCTF{4_P4Rt_1t_i5_30ac9ba3}
...
picoCTF{4_P4Rt_1t_i5_33ba9ac0}
picoCTF{4_P4Rt_1t_i5_30ba3a9c}
picoCTF{4_P4Rt_1t_i5_ba390c3a}
```
While looking through them all I noticed that they all contain the same number of each character seemingly justjumbled up.

The frequence of the character are `2: 3, a. 1: 0, 9, b, c.`

I formatted all the flags in a flags.txt, then I make a simple python script to see the frequency of all the flags:
```py
from collections import defaultdict
freq = defaultdict(int)
with open("flags.txt", "r") as file:
    data = file.read()
    for flag in data.split("\n"):
        freq[flag] += 1
    for k, v in freq.items():
        if v >= 2:
            print(k, v)
```
this printed:
`picoCTF{4_P4Rt_1t_i5_ac3ab903} 2`
This was not the correct flag.

I think I am looking into the wrong thing in this disk. I need to focus on what a disk contains and try to extract that.
