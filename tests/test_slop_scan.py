"""Testes de regressão de scripts/slop_scan.py em texto em português."""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import slop_scan  # noqa: E402


def kinds(text: str, severity: str | None = None) -> list[str]:
    return [
        f.kind
        for f in slop_scan.scan_text(text)
        if severity is None or f.severity == severity
    ]


class AcusaSlop(unittest.TestCase):
    def test_conjugacoes_de_palavras_banidas(self) -> None:
        self.assertEqual(
            kinds("A equipe alavancou as metas, alavancando resultados alavancados."),
            ["banned"] * 3,
        )

    def test_flexao_de_adjetivos(self) -> None:
        self.assertEqual(kinds("Soluções robustas e transformadoras."), ["banned"] * 2)

    def test_alternativas_com_barra(self) -> None:
        self.assertEqual(kinds("Vamos capacitar e empoderar."), ["banned"] * 2)

    def test_travessao_no_meio_da_frase(self) -> None:
        self.assertEqual(kinds("Rápido \u2014 e barato."), ["dash"])

    def test_anglicismo(self) -> None:
        self.assertEqual(kinds("Uma cultura data-driven."), ["anglicism"])

    def test_titulo_em_title_case(self) -> None:
        self.assertEqual(kinds("## O Novo Plano De Lançamento"), ["title_case"])

    def test_expressoes_vigiadas(self) -> None:
        self.assertEqual(
            kinds("Vale ressaltar que funciona. Espero que isso ajude!", "watch"),
            ["phrase", "phrase"],
        )

    def test_contraste_binario(self) -> None:
        self.assertEqual(kinds("Não é sobre velocidade, é sobre confiança."), ["contrast"])

    def test_nao_so_mas(self) -> None:
        self.assertEqual(kinds("Não só rápido, mas barato."), ["contrast"])


class PreservaTextoHumano(unittest.TestCase):
    def test_travessao_de_dialogo(self) -> None:
        self.assertEqual(kinds("\u2014 Não vou, disse ela."), [])

    def test_palavra_citada(self) -> None:
        self.assertEqual(kinds('O chefe vive dizendo "alavancar sinergias".'), [])

    def test_codigo_e_links(self) -> None:
        self.assertEqual(kinds("`robusto` [doc](https://x.com/a--b)"), [])

    def test_hifens_que_nao_sao_jargao(self) -> None:
        self.assertEqual(kinds("Em 2026-10-19 o GPT-4 mandou um e-mail."), [])

    def test_negacao_comum(self) -> None:
        self.assertEqual(kinds("Os preços não são baixos, mas valem a pena."), [])


if __name__ == "__main__":
    unittest.main()
