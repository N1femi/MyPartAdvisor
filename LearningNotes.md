### Terminology
---
**Idiomatic Pandas / Pandorable**: Writing code that leverages panda's built-in vectorized operations rather than looping, this makes processes much faster and cleaner.

**"dunder"**: Double Underscore __

___

**Series**: 1-Dimensional labeled column

**`pd.Series[arrayObj, index=['a','b','c']]`**: Creates Series object from arrayObj with index a, b & c

**`series.loc[index]`**: Returns value of whatever is at that index *aka labels*

**`series.iloc[value]`**: Returns index of value

___
**Dataframe**: 2-Dimensional labeled grid (like excel sheet)

**`df[df[category] >= 20]`**: *Boolean Masking* that acts like a filter returning only rows which the statement is True for.





