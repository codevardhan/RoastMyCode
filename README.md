# RoastMyCode

RoastMyCode is a fun Flask-based application that uses the GPT API to roast and make fun of your code. Simply input your code, and let GPT do the rest. It's a lighthearted way to bring some humor to your coding journey!

## Example

### Input Code

```python
def get_data(url, lang, save_dir, dates):
    header = {"User-Agent": "Mozilla/5.0"}
    url = url.replace("language", args.lang)
    start_date = dates[0]
    end_date = dates[1]
    data = []
    for single_date in daterange(start_date, end_date):
        url_end = single_date.strftime("%Y/%m/%d")
        page_url = url + url_end + "/"
        main_soup = BeautifulSoup(
            requests.get(page_url, headers=header).content, features="lxml"
        )
        check = main_soup.find_all("section")
        if "Page not found" not in check:
            for elem in main_soup.findAll("ul", attrs={"class": "dayindexTitles"}):
                if elem.a:
                    doc_data = ""
                    news_url = url + elem.a.attrs["href"]
                    try:
                        news_soup = BeautifulSoup(
                            requests.get(news_url, headers=header).content,
                            features="lxml",
                        )
                    except e:
                        print(
                            f"Network error, process stopped at url, date: {news_url}, {single_date}"
                        )
                    for elem in news_soup.findAll("p"):
                        doc_data += (
                            str(elem)
                            .replace("\n", "")
                            .replace("<p>", "")
                            .replace("<\\p>", "")
                        )
                    data.append(doc_data)
            with open(os.path.join(save_dir, "monolingual.") + CODES[lang], "w") as f:
                f.writelines(data)
```

### The Roast

![demo](https://github.com/codevardhan/RoastMyCode/assets/52796014/8f84b624-38c1-42f1-a27e-c7df2d57c77d)

## Getting Started

To get started with RoastMyCode, follow these steps:

1. Clone the repository:

```bash
git clone git@github.com:codevardhan/RoastMyCode.git
```


2. Navigate to the project directory:

```bash
cd RoastMyCode
```

3. Create a virtual environment (optional but recommended):

```bash
python3 -m venv venv
source venv/bin/activate
```

4. Install the required dependencies:

```bash
pip install -r requirements.txt
```

5. Set up the GPT API:

- Sign up for an API key at the GPT API website.
- Add your API key to a `.env` file in the project directory:

```
GPT_API_KEY=your-api-key
```

6. Start the Flask application:
```bash
flask run
```

7. Open your web browser and visit `http://localhost:5000` to access the application.

## Usage

1. Enter your code in the provided input field.
2. Click the "Roast Me" button.
3. RoastMyCode will generate a fun and comedic response, making fun of your code.
4. Enjoy the roast and have a good laugh!

## Contributing

If you'd like to contribute to RoastMyCode, feel free to submit a pull request. We welcome any improvements, bug fixes, or additional features.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Acknowledgements

RoastMyCode was inspired by the fun and creative ways to interact with GPT and bring humor to the coding community.
