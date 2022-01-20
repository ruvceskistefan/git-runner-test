import environ
with open(environ['GITHUB_ENV'], 'a') as f:
  subcomment = """\
Please verify the following diffs:
- [ ] All articles ran in 0:00:56.697371: [en](https://wiki.tf/d/3106540) [ar](https://wiki.tf/d/3106518) [cs](https://wiki.tf/d/3106519) [da](https://wiki.tf/d/3106520) [de](https://wiki.tf/d/3106521) [es](https://wiki.tf/d/3106522) [fi](https://wiki.tf/d/3106523) [fr](https://wiki.tf/d/3106524) [hu](https://wiki.tf/d/3106525) [it](https://wiki.tf/d/3106526) [ja](https://wiki.tf/d/3106527) [ko](https://wiki.tf/d/3106528) [nl](https://wiki.tf/d/3106529) [no](https://wiki.tf/d/3106530) [pl](https://wiki.tf/d/3106531) [pt](https://wiki.tf/d/3106532) [pt-br](https://wiki.tf/d/3106533) [ro](https://wiki.tf/d/3106534) [ru](https://wiki.tf/d/3106535) [sv](https://wiki.tf/d/3106536) [tr](https://wiki.tf/d/3106537) [zh-hans](https://wiki.tf/d/3106538) [zh-hant](https://wiki.tf/d/3106539)
- [ ] Wanted templates ran in 0:00:37.264911: [en](https://wiki.tf/d/3106541)"""
  f.write('GITHUB_COMMENT<<EOF')
  f.write(subcomment)
  f.write('EOF')