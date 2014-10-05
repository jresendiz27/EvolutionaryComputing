'''
Super Table
@author: azu
'''
from fitness import * 
import onePlusOne
import muPlusOne
import muPlusLambda

def main():
	fo = open("latex/latex.tex","w+")
	fo.write("\\documentclass[landscape,11pt]{article}\n\\usepackage[landscape]{geometry}\n\\usepackage{graphicx}\n \\setlength{\\topmargin}{-2cm}\n\\setlength{\\textheight}{15cm}\n\\setlength{\\oddsidemargin}{-1cm}\n\\setlength{\\textwidth}{9in}\n\\begin{document}\n\\title{Evolution Strategies}\n \\author{Lopez Garduno Blanca Azucena\\\\ Resendiz Arteaga Juan Alberto}\n \\maketitle\n")
	fo.write("Max. generations: %s Epsilon: %s Sigma: %s Mu: %s Lambda: %s \\\\\n\\begin{tabular}{|c|p{5.4cm}|p{5.4cm}|p{5.4cm}|p{5.4cm}|}\n \\hline\n Func & 1+1 & u+1 & u+h & u,h \\\\ \n \\hline\n"%(maxGenerations,epsilon, sigma[0], mu, lamb))
	for i in range(12,25):
		fo.write(" %s & %s & %s & %s & - \\\\\n \\hline \n"%(i,onePlusOne.onePlusOne(i), muPlusOne.muPlusOne(i), muPlusLambda.muPlusLambda(i)))
	fo.write("\\end{tabular}\n\\end{document}\n")
main()