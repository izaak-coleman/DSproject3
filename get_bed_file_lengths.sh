for base in `cat $1`; do 
  file=$base.bed.gz
  curl -O -L https://www.encodeproject.org/files/$base/@@download/$file
  echo $file >> all_bed_lengths.txt
  gunzip -c $file | wc -l >> all_bed_lengths.txt
  rm $file
done
