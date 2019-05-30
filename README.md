# csv2gpx
This is a small script to convert tracks from a csv into a gpx file

## Installation

* Checkout or download the source
* Change into the directory
* Install the package using the command
  ```bash
  sudo python setup.py install
  ```

## Usage

After you installed the package, you can run it using:
```bash
# python3 -m csv2gpx -h
usage: csv2gpx [-h] [--author AUTHOR] [--url URL] --file FILE
               [--output OUTPUT] [--delimiter DELIMITER]
               [--co-format {DD,DM,DMS}]

Convert a CSV GPS track into a gpx track

optional arguments:
  -h, --help            show this help message and exit
  --author AUTHOR       Set the author tag in metadata
  --url URL             Set the url tag in metadata
  --file FILE           CSV file path
  --output OUTPUT       Output GPX file. If not set, the output is printed to
                        stdout
  --delimiter DELIMITER
                        CSV field delimiter
  --co-format {DD,DM,DMS}
                        Change the coordinate format: DD=decimal degrees
                        (39.5432) / DM=degrees minutes (39°32.592N) /
                        DMS=degrees minutes seconds (39°32'35.52"N)
```

## Input CSV

| track_name    | track_description | date       | time     | time_delta | latitude    | longitude  |
| ------------- | ----------------- | ---------- | -------- | ---------- | ----------- | ---------- |
| track1        | from x to y       | 28.07.2018 | 14:54:23 | 0          | 39.56332885 | 2.63388697 |
| track1        | from x to y       | 28.07.2018 | 15:01:02 | 0          | 39.55658601 | 2.6364467  |
| track2        | from y to z       | 29.07.2018 | 07:13:53 | 0          | 39.53169517 | 2.58579682 |
| track2        | from y to z       | 29.07.2018 | 07:30:43 | 0          | 39.53124451 | 2.58566636 |

### Parameter description

| name                | format |
| ------------------- | ------ |
| track_name          | free text |
| track_description   | free text |
| date                | date in this format (%d.%m.%Y) |
| time                | time in this format (%H:%M:%S) |
| time_delta          | time difference to UTC. 0 means given time is already in UTC |
| latitude            | Either decimal degrees (39.5432) or degrees minutes (39°32.592'N) or degrees minutes seconds (39°32'35.52"N). You have to specify the format as script parameter. By default decimal degrees is used |
| longitude           | Either decimal degrees (39.5432) or degrees minutes (39°32.592'N) or degrees minutes seconds (39°32'35.52"N). You have to specify the format as script parameter. By default decimal degrees is used |

### Resulting GPX
```xml
<?xml version="1.0" ?>
<gpx creator="csv2gpx" version="1.1" xmlns="http://www.topografix.com/GPX/1/1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd">
    <metadata>
        <author>Author</author>
        <link href="https://link-to.authors-website.com"/>
    </metadata>
    <trk>
        <name>track1</name>
        <desc>from x to y</desc>
        <trkseg>
            <trkpt lat="39.56332885" lon="2.63388697">
                <time>2018-07-28T14:54:23+00:00</time>
            </trkpt>
            <trkpt lat="39.55658601" lon="2.6364467">
                <time>2018-07-28T15:01:02+00:00</time>
            </trkpt>
        </trkseg>
    </trk>
    <trk>
        <name>track2</name>
        <desc>from y to z</desc>
        <trkseg>
            <trkpt lat="39.53169517" lon="2.58579682">
                <time>2018-07-29T07:13:53+00:00</time>
            </trkpt>
            <trkpt lat="39.53124451" lon="2.58566636">
                <time>2018-07-29T07:30:43+00:00</time>
            </trkpt>
        </trkseg>
    </trk>
</gpx>
```

## If you think my work was useful for you, you might buy me a beer

[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=LLNQ8N6QKV5GJ&lc=CH&item_name=Mathias%20Schneuwly&item_number=github-csv2gpx&currency_code=CHF)