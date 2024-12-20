import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._groupBox1 = System.Windows.Forms.GroupBox()
        self._groupBox2 = System.Windows.Forms.GroupBox()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._anum = System.Windows.Forms.TextBox()
        self._bnum = System.Windows.Forms.TextBox()
        self._cnum = System.Windows.Forms.TextBox()
        self._acost = System.Windows.Forms.Label()
        self._bcost = System.Windows.Forms.Label()
        self._ccost = System.Windows.Forms.Label()
        self._total = System.Windows.Forms.Label()
        self._groupBox1.SuspendLayout()
        self._groupBox2.SuspendLayout()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.Location = System.Drawing.Point(12, 29)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(100, 23)
        self._label1.TabIndex = 0
        self._label1.Text = "Package A:"
        # 
        # groupBox1
        # 
        self._groupBox1.Controls.Add(self._cnum)
        self._groupBox1.Controls.Add(self._bnum)
        self._groupBox1.Controls.Add(self._anum)
        self._groupBox1.Controls.Add(self._label3)
        self._groupBox1.Controls.Add(self._label2)
        self._groupBox1.Controls.Add(self._label1)
        self._groupBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 11, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._groupBox1.Location = System.Drawing.Point(23, 12)
        self._groupBox1.Name = "groupBox1"
        self._groupBox1.Size = System.Drawing.Size(261, 133)
        self._groupBox1.TabIndex = 1
        self._groupBox1.TabStop = False
        self._groupBox1.Text = "Quantity Sold"
        # 
        # groupBox2
        # 
        self._groupBox2.Controls.Add(self._total)
        self._groupBox2.Controls.Add(self._ccost)
        self._groupBox2.Controls.Add(self._bcost)
        self._groupBox2.Controls.Add(self._acost)
        self._groupBox2.Location = System.Drawing.Point(12, 145)
        self._groupBox2.Name = "groupBox2"
        self._groupBox2.Size = System.Drawing.Size(161, 95)
        self._groupBox2.TabIndex = 2
        self._groupBox2.TabStop = False
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 10, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(199, 162)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(75, 29)
        self._button1.TabIndex = 3
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 10, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(179, 197)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(55, 29)
        self._button2.TabIndex = 4
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 10, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(240, 197)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(55, 29)
        self._button3.TabIndex = 5
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # label2
        # 
        self._label2.Location = System.Drawing.Point(12, 89)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(100, 23)
        self._label2.TabIndex = 1
        self._label2.Text = "Package C:"
        # 
        # label3
        # 
        self._label3.Location = System.Drawing.Point(12, 59)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(100, 23)
        self._label3.TabIndex = 2
        self._label3.Text = "Package B:"
        # 
        # anum
        # 
        self._anum.BackColor = System.Drawing.SystemColors.InactiveCaption
        self._anum.Location = System.Drawing.Point(97, 29)
        self._anum.Name = "anum"
        self._anum.Size = System.Drawing.Size(100, 24)
        self._anum.TabIndex = 3
        # 
        # bnum
        # 
        self._bnum.BackColor = System.Drawing.SystemColors.InactiveCaption
        self._bnum.Location = System.Drawing.Point(97, 59)
        self._bnum.Name = "bnum"
        self._bnum.Size = System.Drawing.Size(100, 24)
        self._bnum.TabIndex = 4
        # 
        # cnum
        # 
        self._cnum.BackColor = System.Drawing.SystemColors.InactiveCaption
        self._cnum.Location = System.Drawing.Point(97, 89)
        self._cnum.Name = "cnum"
        self._cnum.Size = System.Drawing.Size(100, 24)
        self._cnum.TabIndex = 5
        # 
        # acost
        # 
        self._acost.Font = System.Drawing.Font("Microsoft Sans Serif", 9, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._acost.Location = System.Drawing.Point(6, 11)
        self._acost.Name = "acost"
        self._acost.Size = System.Drawing.Size(149, 23)
        self._acost.TabIndex = 6
        self._acost.Text = "Package A:"
        # 
        # bcost
        # 
        self._bcost.Font = System.Drawing.Font("Microsoft Sans Serif", 9, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._bcost.Location = System.Drawing.Point(6, 29)
        self._bcost.Name = "bcost"
        self._bcost.Size = System.Drawing.Size(149, 23)
        self._bcost.TabIndex = 7
        self._bcost.Text = "Package B:"
        # 
        # ccost
        # 
        self._ccost.Font = System.Drawing.Font("Microsoft Sans Serif", 9, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._ccost.Location = System.Drawing.Point(6, 47)
        self._ccost.Name = "ccost"
        self._ccost.Size = System.Drawing.Size(149, 23)
        self._ccost.TabIndex = 8
        self._ccost.Text = "Package C:"
        # 
        # total
        # 
        self._total.Font = System.Drawing.Font("Microsoft Sans Serif", 9, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._total.Location = System.Drawing.Point(6, 65)
        self._total.Name = "total"
        self._total.Size = System.Drawing.Size(149, 23)
        self._total.TabIndex = 9
        self._total.Text = "Grand Total:"
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ActiveCaption
        self.ClientSize = System.Drawing.Size(307, 252)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._groupBox2)
        self.Controls.Add(self._groupBox1)
        self.Name = "MainForm"
        self.Text = "pg269SoftwareSales"
        self._groupBox1.ResumeLayout(False)
        self._groupBox1.PerformLayout()
        self._groupBox2.ResumeLayout(False)
        self.ResumeLayout(False)


    def Button3Click(self, sender, e):
        Application.Exit()

    def Button2Click(self, sender, e):
        self._anum.Text.Clear()
        self._cnum.Text.Clear()
        self._bnum.Text.Clear()
        self._acost.Text = "Package A:"
        self._ccost.Text = "Package C:"
        self._bcost.Text = "Package B:"
        self._total.Text = "Grand Total:"

    def Button1Click(self, sender, e):
        anum = float(self._anum.Text)
        bnum = float(self._bnum.Text)
        cnum = float(self._cnum.Text)
        acost = anum * 99
        bcost = bnum * 199
        ccost = cnum * 299
        
        if anum >= 10 and anum <= 19:
            acost = acost * 0.8
        elif anum >= 20 and anum <= 49:
            acost = acost * 0.7
        elif anum >= 50 and anum <= 99:
            acost = acost * 0.6
        elif anum >= 100:
            acost = acost * 0.5
            
        if bnum >= 10 and bnum <= 19:
            bcost = bcost * 0.8
        elif bnum >= 20 and bnum <= 49:
            bcost = bcost * 0.7
        elif bnum >= 50 and bnum <= 99:
            bcost = bcost * 0.6
        elif bnum >= 100:
            bcost = bcost * 0.5
            
        if cnum >= 10 and cnum <= 19:
            ccost = ccost * 0.8
        elif cnum >= 20 and cnum <= 49:
            ccost = ccost * 0.7
        elif cnum >= 50 and cnum <= 99:
            ccost = ccost * 0.6
        elif cnum >= 100:
            ccost = ccost * 0.5
            
        total = acost + bcost + ccost
        self._acost.Text = "Package A: $" + str(acost)
        self._bcost.Text = "Package B: $" + str(bcost)
        self._ccost.Text = "Package C: $" + str(ccost)
        self._total.Text = "Grand Total: $" + str(total)