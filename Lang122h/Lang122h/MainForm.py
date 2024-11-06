import math 
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._button1 = System.Windows.Forms.Button()
        self._listBox1 = System.Windows.Forms.ListBox()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.SkyBlue
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 14, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(12, 12)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(99, 56)
        self._button1.TabIndex = 0
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # listBox1
        # 
        self._listBox1.BackColor = System.Drawing.SystemColors.InactiveCaption
        self._listBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._listBox1.FormattingEnabled = True
        self._listBox1.ItemHeight = 25
        self._listBox1.Location = System.Drawing.Point(117, 12)
        self._listBox1.Name = "listBox1"
        self._listBox1.Size = System.Drawing.Size(513, 229)
        self._listBox1.TabIndex = 1
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.SkyBlue
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 14, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(12, 74)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(99, 56)
        self._button2.TabIndex = 2
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.LightCoral
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 14, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(12, 136)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(99, 56)
        self._button3.TabIndex = 3
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ActiveCaption
        self.ClientSize = System.Drawing.Size(642, 261)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._listBox1)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "Lang122h"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        num = 0 
        square = 0
        root = 0
        cube = 0
        fourth = 0
        self._listBox1.Items.Add("Number\tSquare\tRoot\tCube\t4th Root")
        while num < 20:
            num = num + 1
            square = num ** 2
            root = math.sqrt(num)
            cube = num ** 3
            fourth = math.sqrt(root)
            root = round(root, 4)
            fourth = round(fourth, 4)
            text = str(num) + "\t" + str(square) + "\t" + str(root) + "\t" + str(cube) + "\t" + str(fourth)
            self._listBox1.Items.Add(text)

    def Button3Click(self, sender, e):
        Application.Exit()

    def Button2Click(self, sender, e):
        self._listBox1.Items.Clear()