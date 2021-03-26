[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

# Missing Column Detection in .csv file

Finding the missing columns based on some formats in a specific dataframe.

## Libraries
```python
from tkinter import filedialog
import tkinter as tk
import pandas as pd
```

## Prerequisites
```python
missing_formats = ["NA", "nan", "NAN", ""]
delimeter = ";" 
```
**missing formats** could be extended depending of needings _i.e. "N.A.", "null", etc._

**delimeter** is mostly notaded by ";" or "," in .csv files.

## Usage
```python
class file_read(object)
  ...
  class miss_columns(file_read) inherited from class file_read(object)
```

```python
print(file_path + " has missing columns : " + ",".join(missing_columns))
```
## Result
_'document_name' has missing columns: ['ColumnA', 'ColumnB',...]_

## Contributing
Pull requests are welcome.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/orkunkus/missing_column_find.svg?style=for-the-badge
[contributors-url]: https://github.com/orkunkus/missing_column_find/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/orkunkus/missing_column_find.svg?style=for-the-badge
[forks-url]: https://github.com/orkunkus/missing_column_find/network/members
[stars-shield]: https://img.shields.io/github/stars/orkunkus/missing_column_find.svg?style=for-the-badge
[stars-url]: https://github.com/orkunkus/missing_column_find/stargazers
[issues-shield]: https://img.shields.io/github/issues/orkunkus/missing_column_find.svg?style=for-the-badge
[issues-url]: https://github.com/orkunkus/missing_column_find/issues
[license-shield]: https://img.shields.io/github/license/orkunkus/missing_column_find.svg?style=for-the-badge
[license-url]: https://github.com/orkunkus/missing_column_find/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/orkunkus


