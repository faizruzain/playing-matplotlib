import matplotlib.pyplot as plt
import pandas as pd
import random
import re

df = pd.read_csv('input/vEdge-02-24-2026.csv')
print(df)
print('\n')

new_data = []
DC = []
DRC = []

for row in df.itertuples(index=False):
    hostname = row[2]
    sn = row[6]
    system_ip = row[7]

    if isinstance(system_ip, float):
        continue
    else:
        DC_patt = '^DC'      
        DRC_patt = '^DRC'      
        bank_code = re.split('\\.', system_ip)
        DC_NAT_RTGS = f'172.20.{bank_code[2]}.232/29, 172.20.{bank_code[2]}.248/29, '
        DC_NAT_Pelaporan = f'172.20.{bank_code[2]}.0/26, 172.20.{bank_code[2]}.64/27, 172.20.{bank_code[2]}.96/27, 172.20.{bank_code[2]}.160/27, '
        DRC_NAT_RTGS = f'172.19.{bank_code[2]}.232/29, 172.19.{bank_code[2]}.248/29, '
        DRC_NAT_Pelaporan = f'172.19.{bank_code[2]}.0/26, 172.19.{bank_code[2]}.64/27, 172.19.{bank_code[2]}.96/27, 172.19.{bank_code[2]}.160/27'

        DC_match = re.match(DC_patt, hostname, flags=0)
        DRC_match = re.match(DC_patt, hostname, flags=0)

        data = {
            'Hostname': hostname,
            'SN': sn,
            'System IP': system_ip,
            'Bank Code': bank_code[2],
            'DC_NAT_RTGS dan Pelaporan': f'{DC_NAT_RTGS} {DC_NAT_Pelaporan}',
            'DRC_NAT_RTGS dan Pelaporan': f'{DRC_NAT_RTGS} {DRC_NAT_Pelaporan}',
        }

        new_data.append(data)

        # if DC_match:
        #     DC_data = {
        #         'Hostname': hostname,
        #         'SN': sn,
        #         'System IP': system_ip,
        #         'Bank Code': bank_code[2],
        #         'DC_NAT_RTGS dan Pelaporan': f'{DC_NAT_RTGS} {DC_NAT_Pelaporan}',
        #         'DRC_NAT_RTGS dan Pelaporan': f'{DRC_NAT_RTGS} {DRC_NAT_Pelaporan}',
        #     }

        #     DC.append(DC_data)

        #     # print(f'system ip: {system_ip} and bank code: {bank_code[2]}')
        #     # print(f'bank code: {bank_code[2]}')
        #     # print(f'DC_NAT_RTGS: {DC_NAT_RTGS}')
        #     # print(f'DC_NAT_Pelaporan: {DC_NAT_Pelaporan}')
        #     # print(f'DRC_NAT_RTGS: {DRC_NAT_RTGS}')
        #     # print(f'DRC_NAT_Pelaporan: {DRC_NAT_Pelaporan}')
        #     # print('\n')

        # if DRC_match:
        #     DRC_data = {
        #         'Hostname': hostname,
        #         'SN': sn,
        #         'System IP': system_ip,
        #         'Bank Code': bank_code[2],
        #         # 'DC_NAT_RTGS dan Pelaporan': f'{DC_NAT_RTGS} {DC_NAT_Pelaporan}',
        #         'DRC_NAT_RTGS dan Pelaporan': f'{DRC_NAT_RTGS} {DRC_NAT_Pelaporan}',
        #     }

        #     DRC.append(DRC_data)

# print(DC_data)
# print(DRC_data)

# DC_data_df = pd.DataFrame(data=DC_data)        
# DRC_data_df = pd.DataFrame(data=DRC_data)

# print(DC_data_df)
# print(DRC_data_df)

new_df = pd.DataFrame(data=new_data,)
new_df.to_csv('output/new_data_2.csv', index=False)

print(new_df)













# Generating dummy data

# traffic_data = {
#     'date': '',
#     'in (Kbps)': 0,
#     'out (Kbps)': 0
# }

# traffic_data_df = pd.DataFrame(traffic_data, index=[0])

# for row in range(31):
#     for column in traffic_data_df.columns:
#         if column == 'date':
#             traffic_data_df.loc[row, column] = row + 1
#         elif column == 'in (Kbps)':
#             traffic_data_df.loc[row, column] = random.randint(0, 100) # random.expovariate()	+ 1
#         elif column == 'out (Kbps)':
#             traffic_data_df.loc[row, column] = random.randint(0, 100) # random.expovariate() + 2

# print(traffic_data_df)
# print('\n')

# # Plotting Traffic Data

# fig, ax = plt.subplots()
# ax.plot('in (Kbps)', data=traffic_data_df, label='Traffic In')
# # ax.plot('out (Kbps)', data=traffic_data_df, label='Traffic Out')
# legend = ax.legend(loc='upper left', shadow=True)

# # Put a nicer background color on the legend.
# legend.get_frame()

# plt.ylabel('Packetloss [%]')
# plt.xlabel('Date')
# plt.show()

# print(f'Traffic in: {traffic_in}')
# print(f'Traffic out: {traffic_out}')

# print(traffic_data_df.get(['in (Kbps)']).iloc[0])
# print(traffic_data_df.get(['in (Kbps)']).iloc[0].iloc[0])