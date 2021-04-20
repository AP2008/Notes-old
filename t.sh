files=(*.md)

for i in "${files[@]}"
do
   echo "$i"
   cd "${i%.*}"
   pandoc --template tem -c https://bootswatch.com/4/sketchy/bootstrap.min.css -s --toc ../"$i" -o "${i%.*}.md.pdf" --pdf-engine wkhtmltopdf
   cd ..
done