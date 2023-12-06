# DATA-MAPPING-
We can connect two data sets with the similarity of strings.
In the codeScript
Primary Dataset = yip
Primary Dataset copied to new_yip
Secondary Dataset=sametham
Secondary Dataset copied=new_sametham

There should be:
<ul>
<li><b>Derived Id_yip</b>
<li><b>Derived_sametham</b>
</ul>


The script checks similarity and finds matches of strings from these columns.So basically you can create Derived Id columns by adding with as much as similar values as possible.The More the Merrier!

Also there should be <b>SL NO</b>
which is a unique identity for the primary dataset.

Basically the script takes two dataets.
Takes one row and from Primary Dataset and from that takes Derived Id column

Then checks it based on the current threshold across all Derived Id of Secondary Dataset. finds the best match and assigns it to mapped data.
When everything is perfectly done,We get 'mapped_data' dataframe as result which contains all the mapped data based on threshold
Thankyou.