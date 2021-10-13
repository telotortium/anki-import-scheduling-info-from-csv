# import the main window object (mw) from aqt
from aqt import mw
from aqt.utils import tooltip
# import all of the Qt GUI library
from aqt.qt import *
from anki import consts

import csv
import os
from datetime import date

def importCSV(reader):
    for row in reader:
        cid, due, ivl, factor, reps = row
        cid = int(cid)
        due = None if due == "" else date.fromisoformat(due)
        ivl = int(float(ivl))
        factor = int(float(factor))
        reps = int(float(reps))
        card = mw.col.get_card(cid)
        if due is None:
            mw.col.sched.schedule_cards_as_new([cid])
        else:
            days = (due - date.today()).days
            card.type = consts.CARD_TYPE_REV
            card.queue = consts.QUEUE_TYPE_REV
            card.due = mw.col.sched.today + days
            card.ivl = ivl
            card.factor = factor
            card.reps = reps
        card.flush()

# We're going to add a menu item below. First we want to create a function to
# be called when the menu item is activated.
def importCSVs():
    mw.importDialog = QFileDialog()
    mw.importDialog.setFileMode(QFileDialog.ExistingFiles)

    if mw.importDialog.exec_():
        fileNames = mw.importDialog.selectedFiles()

        if len(fileNames) > 0:
            for f in fileNames:
                with open(f) as csvfile:
                    importCSV(csv.reader(csvfile))
    mw.col.save()
    mw.reset()
    tooltip("Complete: Import card scheduling info from CSV")

# create a new menu item
action = QAction("Import card scheduling info from CSV", mw)
# set it to call importFromFolder when it's clicked
action.triggered.connect(importCSVs)
# and add it to the tools menu
mw.form.menuTools.addAction(action)
