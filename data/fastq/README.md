# fastq files

Here, raw fastq files were stored. They were sequenced using the NextSeq 500 and still contain adapters. md5 hashes were created using:

```bash
md5sum *.fq.gz
```

19870c16fbac76c45b8e8ad83897ed6a  3_JVpna21.fq.gz
6ec6d59d48dea8bca1edecb3ce40fb7b  3_JVpna22.fq.gz
874f10f03aa39b1e4ce0970493ece914  3_JVpna40.fq.gz
3b4d954efc5ed770b8bae235707dd268  3_JVpna41.fq.gz
4e001533929e15c91de3c114fc62b080  3_JVpna42.fq.gz
30d575b3bf805ad6683a6952e4d7f20f  3_JVpna43.fq.gz
c9ac59c211ef4dd3cc41e9f36f373cbb  3_JVpna44.fq.gz
0f951d865786834cd920996e39b6f24e  3_JVpna47.fq.gz
2089b1d9dac0eed9b38716a5c747413c  3_JVpna48.fq.gz
ab0fc2c0e42431e466f708d638612c00  3_JVpna49.fq.gz
c23d1294c6da318d2c9e1c6546d4ad4b  3_JVpna50.fq.gz
e6766c8ae11b15b76c9fe3497c1141a6  3_JVpna93.fq.gz
f660a467ff6158555a17070acdb90491  3_w_o_control.fq.gz
99efcbe9560178d2caa76952b994e362  hash1_Jvpna93.fq.gz
ebf46bcfe74f1c70b30bce70bbad5b4b  hash1_w_o_control.fq.gz
65dec8084cce21ee82e7a5f245d7f445  hash2_Jvpna93.fq.gz
e25e820ad1056d803b130faee340404f  hash2_w_o_control.fq.gz
0affec3f44c59e88455992368b268ede  L2100396_1_w_o_control.fq.gz
2c8848be0be3a874885d442803a12e3d  L2100397_1_JVpna22.fq.gz
a4b7db0b1b7f6e921390d319f28e4ac0  L2100398_1_JVpna21.fq.gz
cc082015278464e4c5f8b3fce681cb49  L2100400_1_JVpna40.fq.gz
e4a8ce2ccd28a2ca236a4bac9bdfa483  L2100401_1_JVpna41.fq.gz
4b90cc953577376d6f5616fb0cc7a114  L2100402_1_JVpna42.fq.gz
517f4d2b10c08d03d64d4a3677afa491  L2100403_1_JVpna43.fq.gz
b2df61e391fbac43ddd632d9d6c1868d  L2100404_1_JVpna44.fq.gz
5723e99f1184d32527e6725e0c56469e  L2100407_1_JVpna47.fq.gz
b4e11668cbf4c3e6c831a4b14822f72f  L2100408_1_JVpna48.fq.gz
9946c6574a1d9a84d751786d7adabacd  L2100409_1_JVpna49.fq.gz
f398dd45afbbbe8895dae191d464a5ac  L2100410_1_JVpna50.fq.gz
a701ad3c428fbe0cfcb1206d5e47e856  L2100411_2_w_o_control.fq.gz
b472926f83449ca4889c13bdcc8ad467  L2100412_2_JVpna22.fq.gz
4182ad77088480f07f021fde45b15dfd  L2100413_2_JVpna21.fq.gz
78263a40ae7ba7dcfe8e2777af089976  L2100415_2_JVpna40.fq.gz
9f0e4c9c8fc1052d126b2400735f4cb2  L2100416_2_JVpna41.fq.gz
f971ec85ea71eee7dfe81402230d88bf  L2100417_2_JVpna42.fq.gz
41dd7405190a729624503f5a9339c209  L2100418_2_JVpna43.fq.gz
e8b300ed69945a92eeb74970747ef31a  L2100419_2_JVpna44.fq.gz
cd20fc8f0c5c279cc20b1b5d48b3f456  L2100422_2_JVpna47.fq.gz
e5db789be3e1d004bc02f6bcee578e79  L2100423_2_JVpna48.fq.gz
1b9b614a7ec390cee6133b29d0c993d3  L2100424_2_JVpna49.fq.gz
8e66d83a476d808a872e34d20d22b886  L2100425_2_JVpna50.fq.gz



Quality stats can be found in the directory [../../analysis/fastqc](../../analysis/fastqc), and were generated using: 

```bash
fastqc -o ../../analysis/fastqc *.fq.gz
```

