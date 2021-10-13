# Anki Import Scheduling Info From CSV

This is a small addon to reschedule cards based on the contents of a CSV file.
Here is an example CSV:

```
1634097916122,,28.3,1160,43
1634097916110,2021-08-23,28.3,1160,43
```

The meaning of the fields are as follows:

1. Card ID - the ID of the card in question. From [the Anki Add-on
guide](https://addon-docs.ankiweb.net/getting-started.html), here is how you
might discover card IDs for a card from Python.

   ```
   ids = mw.col.find_cards("tag:x")
   ```

   Or you could use [AnkiConnect](https://foosoft.net/projects/anki-connect/).

2. Due date.
   - If blank, makes the card a new card. In this case the rest of the fields
     on the lines are ignored, but they must contain numeric data in order for
     the CSV to be parsed correctly.
   - Otherwise, contains a date in YYYY-MM-DD format to set the due date of the
     card to. In this case, the card is put into the review state.

3. Interval: the interval of the card (i.e., the number of days until the card is due).

4. Ease - the ease of the card. A per-mille value. For example, if you want to
   set your card's ease to 250%, set this field to "2500".

5. Reps - number of times this card has been seen.

## Usage

Once this addon has been installed, a menu item "Import card scheduling info
from CSV" will be added to the "Tools" menu. Click on that, select one or more
CSV files from the file picker, and the card's scheduling information will be
updated. Note that the CSV files must be properly formatted and cannot contain
a header line.

## Motivation

See this Reddit post: [Bulk import notes from another SRS, including setting
scheduling
information](https://www.reddit.com/r/Anki/comments/q3i43n/).

I've been using Org-mode in Emacs for many years now, and I've made many cards
within Org-mode using an SRS package called
[org-drill](https://gitlab.com/phillord/org-drill/). However, I've recently
discovered the [anki-editor](https://github.com/louietan/anki-editor) Emacs
package that lets me manage the contents of the note fields within Org-mode
(next to my other notes) while maintaining the scheduling information in Anki.
Any edits to the note fields within Anki will update the fields in Anki using
AnkiConnect. This has been working very well for me, and I'd like to export my
existing org-drill notes to Anki.

This add-on was written for me to import the scheduling information maintained
by org-drill.

## License

AGPL v3.
