class KontrolaHesla:

    def kontroluj(self,heslo):
    # Podmínky pro heslo
        if len(heslo) > 5 and any(c.isdigit() for c in heslo):
            return True
        else:
            return False


