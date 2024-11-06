import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._listBox1 = System.Windows.Forms.ListBox()
        self._button1 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # listBox1
        # 
        self._listBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._listBox1.FormattingEnabled = True
        self._listBox1.ItemHeight = 20
        self._listBox1.Location = System.Drawing.Point(12, 80)
        self._listBox1.Name = "listBox1"
        self._listBox1.Size = System.Drawing.Size(337, 364)
        self._listBox1.TabIndex = 0
        # 
        # button1
        # 
        self._button1.Location = System.Drawing.Point(12, 12)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(75, 23)
        self._button1.TabIndex = 1
        self._button1.Text = "button1"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(361, 452)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._listBox1)
        self.Name = "MainForm"
        self.Text = "Lang122i"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        num = -26
        croot = 0
        cube = 0
        self._listBox1.Items.Add("Number\tCube Root\tCube")
        while num < 25:
            num = num + 1
            croot = num ** 1./3.
            cube = num ** 3
            croot = round(croot, 5)
            text = str(num) + "\t" + str(croot) + "\t\t" + str(cube)
            self._listBox1.Items.Add(text)
            