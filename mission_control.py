import random
import copy

# =================================== DADOS  ========================================================

# nome da missao -> nome da equipe
missao_info = ["Missão Space Helper Companion","Equipe Horizon Z"]

"""
Abaixo está como a matriz é interpretada
dados_missao = [
 [temperatura, comunicacao, bateria, oxigenio, estabilidade],
 [temperatura, comunicacao, bateria, oxigenio, estabilidade],
 [temperatura, comunicacao, bateria, oxigenio, estabilidade],
 [temperatura, comunicacao, bateria, oxigenio, estabilidade],
 [temperatura, comunicacao, bateria, oxigenio, estabilidade],
 [temperatura, comunicacao, bateria, oxigenio, estabilidade]
]
"""
dados_missao = [
 [24, 92, 88, 96, 90],
 [27, 80, 72, 94, 85],
 [31, 65, 58, 91, 70],
 [36, 42, 38, 87, 55],
 [39, 28, 19, 78, 35],
 [34, 55, 32, 82, 50]
]

areas_monitoradas = [
 "Temperatura interna",
 "Comunicação com a base",
 "Sistema de energia",
 "Suporte de oxigênio",
 "Estabilidade operacional"
]

"""
Abaixo estão os alertas do ciclo, e como eles são interpretados
0 = Normal
1 = Atenção
2 = crítico
"""
alertas = [
 [0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0]
]

pilha_historico = []
possivel_salvar=True

# =================================== FUNÇÕES AUXILIARES  ========================================================

# Função para geração aleatória dos números
def gerar_random(seed_usada):
  random.seed(seed_usada)
  for fileira in range(0,6):
    for coluna in range(0,5):
      dados_missao[fileira][coluna] = round(random.uniform(0,100),2)
    print (dados_missao[fileira])

# Função para ler textos
def status_texto(nivel_alerta):
    if nivel_alerta == 0:
        return "NORMAL"
    elif nivel_alerta == 1:
        return "ATENÇÃO"
    else:
        return "CRÍTICO"

# Função para chamar as funções de analise
def analise_completa():
    for fileira in range(6):
        analisar_temperatura(fileira)
        analisar_comunicacao(fileira)
        analisar_bateria(fileira)
        analisar_oxigenio(fileira)
        analisar_estabilidade(fileira)

# Função para salvar o histórico
def salvar_historico():
    registro = {
        "missao": missao_info[0],
        "equipe": missao_info[1],
        "dados": copy.deepcopy(dados_missao),
        "alertas": copy.deepcopy(alertas)
    }
    pilha_historico.append(registro)
    print("\nDados e alertas atuais salvos na Pilha de Histórico com sucesso!")

# =================================== MENUS ========================================================

# Menu principal onde o usuário poderá realizar todas as decisões
def menu_main():
    while True:
        print("\n╔════════════════════════════════════════╗")
        print("║   Mission Control APP — GS 2026        ║")
        print("╠════════════════════════════════════════╣")
        print("║   1.  Gerar dados simulados            ║")
        print("║   2.  Gerar relatório dos ciclos       ║")
        print("║   3.  Histórico das leituras           ║")
        print("║   0.  Sair                             ║")
        print("╚════════════════════════════════════════╝")
        print(f"Missão: {missao_info[0]}\nEquipe: {missao_info[1]}\n{'═'*40}")
        escolha = input("\nSua escolha (0-3): ").strip()
        match escolha:
          case "0":
            print("\nEncerrando o Mission Control AI.")
            break
          case "1":
            menu_geracaoDados()
          case "2":
            menu_relatorios()
          case "3":
            menu_historico()
          case _:
            print("Opção inválida! Digite 0, 1, 2 ou 3.")

def menu_historico():
    global dados_missao, alertas
    while True:
        print("\n╔════════════════════════════════════════╗")
        print("║         HISTÓRICO DE LEITURAS          ║")
        print("╠════════════════════════════════════════╣")
        print("║   1.  Ver relatórios salvos            ║")
        print("║   2.  Restaurar dados de um histórico  ║")
        print("║   3.  Apagar um histórico específico   ║")
        print("║   0.  Voltar                           ║")
        print("╚════════════════════════════════════════╝")
        escolha = input("\nSua escolha (0-3): ").strip()
        match escolha:
            case "0":
                break
            case "1":
                if len(pilha_historico) == 0:
                    print("\n Nenhum dado foi salvo no histórico ainda.")
                else:
                    print("\n" + "=" * 50)
                    print("HISTÓRICO SALVO (Do mais recente ao mais antigo)")
                    print("=" * 50)
                    for idx, registro in reversed(list(enumerate(pilha_historico))):
                        print(f"\n[ RELATÓRIO SALVO #{idx + 1} ]")
                        print(f"Missão: {registro['missao']} | Equipe: {registro['equipe']}")
                        print("Leituras registradas no momento:")
                        for ciclo in range(6):
                            temp = f"{registro['dados'][ciclo][0]:.2f}"
                            com = f"{registro['dados'][ciclo][1]:.2f}"
                            bat = f"{registro['dados'][ciclo][2]:.2f}"
                            o2 = f"{registro['dados'][ciclo][3]:.2f}"
                            est = f"{registro['dados'][ciclo][4]:.2f}"
                            print(f"  Ciclo {ciclo + 1} -> Temp: {temp} | Com: {com} | Bat: {bat} | O2: {o2} | Est: {est}")
            case "2":
                if len(pilha_historico) == 0:
                    print("\n Nenhum dado no histórico para restaurar.")
                    continue
                id_restaurar = input("\nDigite o número do relatório que deseja TORNAR ATUAL: ")
                try:
                    idx = int(id_restaurar) - 1
                    if 0 <= idx < len(pilha_historico):
                        dados_missao = copy.deepcopy(pilha_historico[idx]["dados"])
                        alertas = copy.deepcopy(pilha_historico[idx]["alertas"])
                        print(
                            f"\nOs dados do relatório {idx + 1} agora são os dados ativos da simulação.")
                    else:
                        print("\nID não encontrado no histórico.")
                except ValueError:
                    print("\nDigite um número válido.")
            case "3":
                if len(pilha_historico) == 0:
                    print("\nNenhum dado no histórico para apagar.")
                    continue
                id_apagar = input("\nDigite o número do relatório que deseja APAGAR: ")
                try:
                    idx = int(id_apagar) - 1
                    if 0 <= idx < len(pilha_historico):
                        pilha_historico.pop(idx)
                        print(f"\nO relatório #{idx + 1} foi permanentemente apagado do histórico.")
                    else:
                        print("\nID não encontrado no histórico.")
                except ValueError:
                    print("\nPor favor, digite um número válido.")

            case _:
                print("\nOpção inválida! Digite 0, 1, 2 ou 3.")

# Menu da geração de dados
def menu_geracaoDados():
    global possivel_salvar
    while True:
          print("\n╔════════════════════════════════════════╗")
          print("║           GERAÇÃO DE DADOS             ║")
          print("╠════════════════════════════════════════╣")
          print("║   1.  Gerar dados aleatórios           ║")
          print("║   2.  Gerar dados em seed              ║")
          print("║   3.  Definir dados manualmente        ║")
          print("║   4.  Visualizar dados atuais          ║")
          print("║   5.  Mudar nome de equipe e missão    ║")
          print("║   0.  voltar                           ║")
          print("╚════════════════════════════════════════╝")
          escolha = input("\nEscolha uma forma de gerar os dados da missão para o teste do aplicativo.(0-5): ").strip()
          match escolha:
            case "0":
              break
            case "1":
              seed_random = random.randint(0,100)
              print(f"\nOs dados serão gerados de forma aleatória usando a seed {seed_random}")
              gerar_random(seed_random)
              analise_completa()
              possivel_salvar = True
            case "2":
              while True:
                seed_random = input("\nDigite a seed numérica em um valor inteiro: ")
                try:
                    seed_number = int(seed_random)
                    break
                except ValueError:
                    print("Erro: todos os valores devem ser numéricos inteiros.")
                    continue
              gerar_random(seed_number)
              analise_completa()
              possivel_salvar = True
            case "3":
              print("\nOs dados correspondem a seguinte ordem:\ntemperatura, comunicacao, bateria, oxigenio, estabilidade")
              for fileira in range(0,6):
                # validação se é 5 números e se só foi escrito digitos
                while True:
                  manual_gerar = input(f"\nCiclo {fileira+1}:\nDigite cada número separado por vírgula\nExemplo: 89,40,60,50,40: ").split(',')
                  if len(manual_gerar)!= 5:
                      print("Número de dados inválido, é necessário 5 dados numéricos")
                      continue
                  try:
                      for coluna in range(0, 5):
                          dados_missao[fileira][coluna] = float(manual_gerar[coluna])
                      break
                  except ValueError:
                        print("Erro: todos os valores devem ser numéricos.")
              analise_completa()
              possivel_salvar = True
            case "4":
              for ciclos in range(0, len(dados_missao)):
                  print(f"Ciclo {ciclos + 1}\n{'=' * 30}")
                  print(f"Temperatura: {dados_missao[ciclos][0]}")
                  print(f"Comunicação: {dados_missao[ciclos][1]}")
                  print(f"Bateria: {dados_missao[ciclos][2]}")
                  print(f"Oxigênio: {dados_missao[ciclos][3]}")
                  print(f"Estabilidade: {dados_missao[ciclos][4]}")
            case "5":
                global  missao_info
                missao_info[0] = input("Digite o Nome da missão: ")
                missao_info[1] = input("Digite o Nome da Equipe: ")
                while True:
                    if missao_info[0] == "":
                        missao_info[0] = input("Nome da missão vazio, digite um nome para a missão: ")
                        continue
                    if missao_info[1] == "":
                        missao_info[1] = input("Nome da equipe vazio, digite um nome para a equipe: ")
                        continue
                    break
            case _:
              print("Opção inválida! Digite 0, 1, 2 ou 3.")

def menu_relatorios():
    global possivel_salvar
    while True:
          print("\n╔════════════════════════════════════════╗")
          print("║               RELATÓRIOS               ║")
          print("╠════════════════════════════════════════╣")
          print("║   1.  visualizar ciclo específico      ║")
          print("║   2.  Gerar relatório geral            ║")
          print("║   3.  status das áreas                 ║")
          print("║   0.  voltar                           ║")
          print("╚════════════════════════════════════════╝")
          escolha = input("\nSua escolha (0-3): ").strip()
          match escolha:
            case "0":
              break
            case "1":
              print(f"\nMissão: {missao_info[0]}\nEquipe: {missao_info[1]}\nQuantidade de ciclos analisados: 1")
              while True:
                  ciclo_escolhido = input("digite um número de 1 à 6 para gerar o relatório do ciclo: ")
                  try:
                      ciclo_valor_num = int(ciclo_escolhido)
                  except ValueError:
                      print("Erro: todos os valores devem ser numéricos.")
                      continue
                  if 1 <= ciclo_valor_num <= 6:
                      gerar_relatorio_ciclo(ciclo_valor_num - 1)
                      break
                  else:
                      print("Erro: o valor deve ser de 1 à 6")
              if possivel_salvar == True:
                  salvar_historico()
                  possivel_salvar = False
            case "2":
              print(f"\nMissão: {missao_info[0]}\nEquipe: {missao_info[1]}\nQuantidade de ciclos analisados: 6")
              for ciclos in range(0,6):
                gerar_relatorio_ciclo(ciclos)
              relatorios_gerais()
              if possivel_salvar == True:
                salvar_historico()
                possivel_salvar = False
            case "3":
                  while True:
                      print("\nÁREAS MONITORADAS")
                      print("=" * 40)

                      for i in range(len(areas_monitoradas)):
                          print(f"{i + 1}. {areas_monitoradas[i]}")

                      print("0. Voltar")
                      escolha_area = input("\nEscolha uma área: ")
                      try:
                          escolha_area = int(escolha_area)
                          if escolha_area == 0:
                              break
                          if 1 <= escolha_area <= 5:
                              print(f"\nMissão: {missao_info[0]}\nEquipe: {missao_info[1]}\nQuantidade de áreas analisadas: 1")
                              relatorio_area(escolha_area - 1)
                              break
                          else:
                              print("Digite um valor entre 1 e 5.")
                      except ValueError:
                          print("Digite apenas números.")
                  if possivel_salvar == True:
                      salvar_historico()
                      possivel_salvar = False
            case _:
              print("Opção inválida! Digite 0, 1, 2 ou 3.")


# =================================== FUNÇÕES ANÁLISE  ========================================================

def analisar_temperatura(ciclo_analisado):
  if dados_missao[ciclo_analisado][0] < 18:
    alertas[ciclo_analisado][0] = 1
  elif dados_missao[ciclo_analisado][0] >= 18 and dados_missao[ciclo_analisado][0]<30:
    alertas[ciclo_analisado][0] = 0
  elif dados_missao[ciclo_analisado][0] >= 30 and dados_missao[ciclo_analisado][0]<35:
    alertas[ciclo_analisado][0] = 1
  else:
    alertas[ciclo_analisado][0] = 2

def analisar_comunicacao(ciclo_analisado):
  if dados_missao[ciclo_analisado][1] >= 60:
    alertas[ciclo_analisado][1] = 0
  elif dados_missao[ciclo_analisado][1] < 30:
    alertas[ciclo_analisado][1] = 2
  else:
    alertas[ciclo_analisado][1] = 1

def analisar_bateria(ciclo_analisado):
  if dados_missao[ciclo_analisado][2] >=50:
    alertas[ciclo_analisado][2] = 0
  elif dados_missao[ciclo_analisado][2] < 20:
    alertas[ciclo_analisado][2] = 2
  else:
    alertas[ciclo_analisado][2] = 1

def analisar_oxigenio(ciclo_analisado):
  if dados_missao[ciclo_analisado][3] >=90:
    alertas[ciclo_analisado][3] = 0
  elif dados_missao[ciclo_analisado][3] < 80:
    alertas[ciclo_analisado][3] = 2
  else:
    alertas[ciclo_analisado][3] = 1

def analisar_estabilidade(ciclo_analisado):
  if dados_missao[ciclo_analisado][4] >=70:
    alertas[ciclo_analisado][4] = 0
  elif dados_missao[ciclo_analisado][4] < 40:
    alertas[ciclo_analisado][4] = 2
  else:
    alertas[ciclo_analisado][4] = 1

def classificar_ciclo(ciclo_analisado):
    estado_missao = sum(alertas[ciclo_analisado])
    if estado_missao <= 2:
      return "MISSÃO ESTÁVEL"
    elif estado_missao > 2 and estado_missao <=5:
      return "MISSÃO EM ATENÇÃO"
    else:
      return "MISSÃO CRÍTICA"

def area_maior_risco():
    pontuacao_areas = [0] * 5

    for ciclo in alertas:
        for area in range(5):
            pontuacao_areas[area] += ciclo[area]
    maior_pontuacao = max(pontuacao_areas)
    areas_mais_afetadas = []

    for i in range(len(pontuacao_areas)):
        if pontuacao_areas[i] == maior_pontuacao:
            areas_mais_afetadas.append(areas_monitoradas[i])
    return pontuacao_areas, areas_mais_afetadas

def analisar_tendencia_por_ciclo(ciclo_anterior, ciclo_atual):
    print(f"\n{'-' * 50}\nAnálise de estabilidade por área (Ciclo {ciclo_anterior + 1} para o Ciclo {ciclo_atual + 1})")
    risco_anterior = sum(alertas[ciclo_anterior])
    risco_atual = sum(alertas[ciclo_atual])

    # Tendência geral
    if risco_atual > risco_anterior:
        print("Tendência geral: Piorou comparado ao ciclo anterior\n")
    elif risco_atual < risco_anterior:
        print("Tendência geral: Melhorou comparado ao ciclo anterior\n")
    else:
        print("Tendência geral: Se manteve estável comparado ao ciclo anterior\n")

    nomes_areas = ["Temperatura", "Comunicação", "Bateria", "Oxigênio", "Estabilidade"]

    for area in range(5):
        risco_ant = alertas[ciclo_anterior][area]
        risco_atu = alertas[ciclo_atual][area]

        # Compara os riscos
        if risco_atu > risco_ant:
            status = "Piorou (Aumento no nível de risco)"
        elif risco_atu < risco_ant:
            status = "Melhorou (Sistemas estabilizando)"
        else:
            status = "Estável (Manteve o nível de atenção/crítico ou normal)"
        print(f"{nomes_areas[area]}: {status}")

# =================================== FUNÇÕES RECOMENDAÇÕES e estabilidade  ========================================================

def estabilidade_temperatura(ciclo_analisado):
    temperatura = alertas[ciclo_analisado][0]
    match temperatura:
        case 0:
            return "Temperatura estável"
        case 1:
            if dados_missao[ciclo_analisado][0] < 18:
                return "temperatura abaixo do normal"
            else:
                return "temperatura elevada"
        case 2:
            return "risco de superaquecimento"

def estabilidade_comunicacao(ciclo_analisado):
    comunicacao = alertas[ciclo_analisado][1]
    match comunicacao:
        case 0:
            return "Comunicação estável"
        case 1:
            return "Sinal instável ou latência alta"
        case 2:
            return "Perda crítica de conexão"

def estabilidade_bateria(ciclo_analisado):
    bateria = alertas[ciclo_analisado][2]
    match bateria:
        case 0:
            return "Bateria em nível seguro"
        case 1:
            return "Nível de energia baixo/moderado"
        case 2:
            return "Risco crítico de apagão"

def estabilidade_oxigenio(ciclo_analisado):
    oxigenio = alertas[ciclo_analisado][3]
    match oxigenio:
        case 0:
            return "Oxigênio adequado"
        case 1:
            return "Variação detectada nos níveis de oxigênio"
        case 2:
            return "Pressão crítica: falha no suporte de vida"

def estabilidade_operacional(ciclo_analisado):
    estabilidade = alertas[ciclo_analisado][4]
    match estabilidade:
        case 0:
            return "Estabilidade operacional adequada"
        case 1:
            return "Instabilidade orbital/física detectada"
        case 2:
            return "Risco de falha estrutural ou capotamento"


def gerar_recomendacao(ciclo_analisado):
    estado_missao = sum(alertas[ciclo_analisado])
    recomendacoes = []

    if estado_missao == 0:
        recomendacoes.append("GERAL: Tudo operando de forma nominal. Manter o curso.")
    elif estado_missao <= 2:
        recomendacoes.append("GERAL: Monitorar variações de perto, mas sem necessidade de intervenção imediata.")
    elif estado_missao <= 5:
        recomendacoes.append("GERAL: Atenção necessária. Realizar diagnósticos nos sistemas com alertas ativos.")
    else:
        recomendacoes.append("GERAL: ALERTA! Abortar operação ou ativar protocolos de emergência imediatamente!")

    if alertas[ciclo_analisado][0] == 1:
        if dados_missao[ciclo_analisado][0] < 18:
            recomendacoes.append("- TEMPERATURA: Aumentar aquecimento dos trajes e painéis internos.")
        else:
            recomendacoes.append("- TEMPERATURA: Verificar controle térmico e acionar resfriamento primário.")
    elif alertas[ciclo_analisado][0] == 2:
         recomendacoes.append("- TEMPERATURA (CRÍTICO): Risco de superaquecimento! Evacuar área e acionar resfriamento de emergência.")

    if alertas[ciclo_analisado][1] == 1:
         recomendacoes.append("- COMUNICAÇÃO: Realizar calibração de antena e tentar isolar interferências de sinal.")
    elif alertas[ciclo_analisado][1] == 2:
         recomendacoes.append("- COMUNICAÇÃO (CRÍTICO): Conexão perdida! Ativar transmissores de backup e disparar sinalizador.")

    if alertas[ciclo_analisado][2] == 1:
         recomendacoes.append("- BATERIA: Desativar sistemas de suporte não essenciais para conservação de energia.")
    elif alertas[ciclo_analisado][2] == 2:
         recomendacoes.append("- BATERIA (CRÍTICO): Risco de apagão total! Acionar geradores de reserva imediatamente.")

    if alertas[ciclo_analisado][3] == 1:
         recomendacoes.append("- OXIGÊNIO: Inspecionar filtros de CO2 e recalibrar misturadores de gás.")
    elif alertas[ciclo_analisado][3] == 2:
         recomendacoes.append("- OXIGÊNIO (CRÍTICO): Falha no suporte de vida! Vestir trajes pressurizados e abrir cilindros O2 reserva.")

    if alertas[ciclo_analisado][4] == 1:
         recomendacoes.append("- ESTABILIDADE: Ajustar giroscópios e recalibrar propulsores de estabilização lateral.")
    elif alertas[ciclo_analisado][4] == 2:
         recomendacoes.append("- ESTABILIDADE (CRÍTICO): Risco estrutural iminente! Preparar para impacto ou abortar manobra.")
    return "\n  ".join(recomendacoes)

# =================================== RELATÓRIOS  ========================================================


def gerar_relatorio_ciclo(ciclo_analisado):
  print(f"\n{'='*50}\nCiclo {ciclo_analisado+1}\n")
  print(f"Temperatura: {dados_missao[ciclo_analisado][0]} | {status_texto(alertas[ciclo_analisado][0])} | {estabilidade_temperatura(ciclo_analisado)}")
  print(f"Comunicação: {dados_missao[ciclo_analisado][1]} | {status_texto(alertas[ciclo_analisado][1])} | {estabilidade_comunicacao(ciclo_analisado)}")
  print(f"Bateria: {dados_missao[ciclo_analisado][2]} | {status_texto(alertas[ciclo_analisado][2])} | {estabilidade_bateria(ciclo_analisado)}")
  print(f"Oxigênio: {dados_missao[ciclo_analisado][3]} | {status_texto(alertas[ciclo_analisado][3])} | {estabilidade_oxigenio(ciclo_analisado)}")
  print(f"Estabilidade: {dados_missao[ciclo_analisado][4]} | {status_texto(alertas[ciclo_analisado][4])} | {estabilidade_operacional(ciclo_analisado)}")

  print(f"\nPontuação de risco do ciclo: {sum(alertas[ciclo_analisado])}")
  print(f"Classificação do ciclo: {classificar_ciclo(ciclo_analisado)}")
  print(f"Recomendações:\n  {gerar_recomendacao(ciclo_analisado)}")
  if ciclo_analisado > 0:
      analisar_tendencia_por_ciclo(ciclo_analisado - 1, ciclo_analisado)

def relatorios_gerais():
    pontuacoes, areas_criticas = area_maior_risco()

    print(f"\n{'=' * 50}\nIDENTIFICAÇÃO DA ÁREA MAIS AFETADA\n")

    for i in range(5):
        print(f"{areas_monitoradas[i]}: {pontuacoes[i]} pontos")
    print("\nÁrea(s) mais afetada(s):")
    for area in areas_criticas:
        print(f"- {area}")

def relatorio_area(area):
    print("\n" + "=" * 60)
    print(f"ANÁLISE DA ÁREA: {areas_monitoradas[area].upper()}")
    print("=" * 60)

    historico = []

    for ciclo in range(6):
        historico.append(alertas[ciclo][area])

    normais = historico.count(0)
    atencoes = historico.count(1)
    criticos = historico.count(2)

    melhoras = 0
    pioras = 0

    pior_momento = 0
    maior_risco = historico[0]

    for ciclo in range(1, 6):

        if historico[ciclo] > historico[ciclo - 1]:
            pioras += 1

        elif historico[ciclo] < historico[ciclo - 1]:
            melhoras += 1

        if historico[ciclo] > maior_risco:
            maior_risco = historico[ciclo]
            pior_momento = ciclo

    print("\nResumo dos ciclos")
    print("-" * 30)

    print(f"Normais : {normais}")
    print(f"Atenções: {atencoes}")
    print(f"Críticos : {criticos}")

    print(f"\nMelhoras registradas: {melhoras}")
    print(f"Pioras registradas : {pioras}")

    print("\nHistórico:")
    for ciclo in range(6):
        print(
            f"Ciclo {ciclo+1}: "
            f"{status_texto(historico[ciclo])}"
        )

    print("\nPior momento:")
    print(
        f"Ciclo {pior_momento+1} "
        f"({status_texto(maior_risco)})"
    )

    print("\nConclusão:")
    if criticos >= 3:
        print(
            "A área apresentou falhas recorrentes e "
            "permaneceu em condição crítica durante "
            "parte significativa da missão."
        )

    elif pioras > melhoras:
        print(
            "A área demonstrou degradação progressiva "
            "ao longo dos ciclos, exigindo monitoramento."
        )

    elif melhoras > pioras:
        print(
            "A área apresentou recuperação gradual "
            "e sinais de estabilização ao longo da missão."
        )

    else:
        print(
            "A área manteve comportamento relativamente "
            "estável durante a missão."
        )

    if historico[-1] < historico[0]:
        print(
            "O sistema terminou em condição melhor "
            "do que a observada no início."
        )

    elif historico[-1] > historico[0]:
        print(
            "O sistema terminou em condição pior "
            "do que a observada no início."
        )
  # =================================== INÍCIO EXECUÇÃO  ========================================================
analise_completa()
menu_main()