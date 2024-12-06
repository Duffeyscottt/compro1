import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._calc = System.Windows.Forms.Button()
        self._clear = System.Windows.Forms.Button()
        self._exit = System.Windows.Forms.Button()
        self._perc = System.Windows.Forms.Label()
        self._calor = System.Windows.Forms.TextBox()
        self._fat = System.Windows.Forms.TextBox()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.PaleTurquoise
        self._label1.Font = System.Drawing.Font("Lucida Sans", 9, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(26, 24)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(158, 30)
        self._label1.TabIndex = 0
        self._label1.Text = "Enter the number of calories in the food:"
        self._label1.TextAlign = System.Drawing.ContentAlignment.BottomRight
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.PaleTurquoise
        self._label2.Font = System.Drawing.Font("Lucida Sans", 9, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(26, 63)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(158, 33)
        self._label2.TabIndex = 1
        self._label2.Text = "Enter the number of fat grams in the food:"
        self._label2.TextAlign = System.Drawing.ContentAlignment.BottomRight
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.PaleTurquoise
        self._label3.Font = System.Drawing.Font("Lucida Sans", 9, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(26, 119)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(158, 35)
        self._label3.TabIndex = 2
        self._label3.Text = "Percentage of calories that come from fat:"
        self._label3.TextAlign = System.Drawing.ContentAlignment.BottomRight
        # 
        # calc
        # 
        self._calc.Font = System.Drawing.Font("Lucida Sans", 9, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._calc.Location = System.Drawing.Point(47, 174)
        self._calc.Name = "calc"
        self._calc.Size = System.Drawing.Size(79, 23)
        self._calc.TabIndex = 3
        self._calc.Text = "Calculate"
        self._calc.UseVisualStyleBackColor = True
        self._calc.Click += self.CalcClick
        # 
        # clear
        # 
        self._clear.Font = System.Drawing.Font("Lucida Sans", 9, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._clear.Location = System.Drawing.Point(132, 174)
        self._clear.Name = "clear"
        self._clear.Size = System.Drawing.Size(75, 23)
        self._clear.TabIndex = 4
        self._clear.Text = "Clear"
        self._clear.UseVisualStyleBackColor = True
        self._clear.Click += self.Button2Click
        # 
        # exit
        # 
        self._exit.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._exit.Font = System.Drawing.Font("Lucida Sans", 9, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._exit.Location = System.Drawing.Point(213, 174)
        self._exit.Name = "exit"
        self._exit.Size = System.Drawing.Size(75, 23)
        self._exit.TabIndex = 5
        self._exit.Text = "Exit"
        self._exit.UseVisualStyleBackColor = False
        self._exit.Click += self.Button3Click
        # 
        # perc
        # 
        self._perc.BackColor = System.Drawing.Color.White
        self._perc.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._perc.Font = System.Drawing.Font("Lucida Sans", 9, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._perc.Location = System.Drawing.Point(190, 131)
        self._perc.Name = "perc"
        self._perc.Size = System.Drawing.Size(116, 23)
        self._perc.TabIndex = 6
        self._perc.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # calor
        # 
        self._calor.Font = System.Drawing.Font("Lucida Sans", 9, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._calor.Location = System.Drawing.Point(190, 32)
        self._calor.Name = "calor"
        self._calor.Size = System.Drawing.Size(116, 22)
        self._calor.TabIndex = 7
        # 
        # fat
        # 
        self._fat.Font = System.Drawing.Font("Lucida Sans", 9, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._fat.Location = System.Drawing.Point(190, 74)
        self._fat.Name = "fat"
        self._fat.Size = System.Drawing.Size(116, 22)
        self._fat.TabIndex = 8
        self._fat.TextChanged += self.TextBox2TextChanged
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.DarkCyan
        self.ClientSize = System.Drawing.Size(337, 209)
        self.Controls.Add(self._fat)
        self.Controls.Add(self._calor)
        self.Controls.Add(self._perc)
        self.Controls.Add(self._exit)
        self.Controls.Add(self._clear)
        self.Controls.Add(self._calc)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Pg268FatCalc"
        self.ResumeLayout(False)
        self.PerformLayout()


    def TextBox2TextChanged(self, sender, e):
        pass

    def Button3Click(self, sender, e):
        Application.Exit()

    def Button2Click(self, sender, e):
        self._calor.Clear()
        self._fat.Clear()
        self._perc.Text = ""

    def CalcClick(self, sender, e):
        calor = float(self._calor.Text)
        fat = float(self._fat.Text)
        cff = fat * 9
        if calor < 1 or fat < 1:
            MessageBox.Show("Numbers must not be less than one", "Input Error")
        elif cff > calor:
            MessageBox.Show("Calories from fat cannot be greater than total calories", "Error")
        else:
            perc = cff / calor
            perc = perc * 100
            self._perc.Text = str(round(perc, 2)) + "%"
            if perc <= 30:
                MessageBox.Show("Food is low in fat")