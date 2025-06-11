import { Box, Grid, Paper, Typography } from '@mui/material'
import Chart from '../components/Chart'
import CustomCard from '../components/CustomCard'

const Dashboard = () => {
  return (
    <Box sx={{
        padding: 2,
        minHeight: '100vh',
        width: '100vw',
        boxSizing: 'border-box',
        overflow: 'hidden'
    }}>
        <Typography variant="h2" fontWeight={700}>Dashboard</Typography>
        
        <Grid container spacing={2} mt={2} sx={{ height: '50%' }}>
          <Grid size={{xs: 12, sm: 6, md: 3 }}>
            <Paper elevation={4} sx={{ padding: 2, borderRadius: 5, transition: "box-shadow 0.3s",
              "&:hover": {
                boxShadow: 6,
              }, }}>
              <Typography variant="h5">KPI 1</Typography>
              <CustomCard title="99" />
            </Paper>
          </Grid>
          <Grid size={{xs: 12, sm: 6, md: 3 }}>
            <Paper elevation={4} sx={{ padding: 2, borderRadius: 5, transition: "box-shadow 0.3s",
              "&:hover": {
                boxShadow: 6,
              }, }}>
              <Typography variant="h5">KPI 2</Typography>
              <CustomCard title="99" />
            </Paper>
          </Grid>
          <Grid size={{xs: 12, sm: 6, md: 3 }}>
            <Paper elevation={4} sx={{ padding: 2, borderRadius: 5, transition: "box-shadow 0.3s",
              "&:hover": {
                boxShadow: 6,
              }, }}>
              <Typography variant="h5">KPI 3</Typography>
              <CustomCard title="99" />
            </Paper>
          </Grid>
          <Grid size={{xs: 12, sm: 6, md: 3 }}>
            <Paper elevation={4} sx={{ padding: 2, borderRadius: 5, transition: "box-shadow 0.3s",
              "&:hover": {
                boxShadow: 6,
              }, }}>
              <Typography variant="h5">KPI 4</Typography>
              <CustomCard title="99" />
            </Paper>
          </Grid>
        </Grid>

        {/* Métricas - 2 cards na parte inferior ocupando toda a largura */}
        <Grid container spacing={2} mt={2}>
          <Grid size={{xs: 12, md: 6 }}>
            <Paper elevation={4} sx={{ padding: 2, borderRadius: 5, transition: "box-shadow 0.3s",
              "&:hover": {
                boxShadow: 6,
              }, }}>
              <Typography variant="h5">Métrica 1</Typography>
              <Chart/>
            </Paper>
          </Grid>
          <Grid size={{xs: 12, md: 6 }}>
            <Paper elevation={4} sx={{ padding: 2, borderRadius: 5, transition: "box-shadow 0.3s",
              "&:hover": {
                boxShadow: 6,
              }, }}>
              <Typography variant="h5">Métrica 2</Typography>
              <Chart/>
            </Paper>
          </Grid>
        </Grid>
    </Box>
  )
}

export default Dashboard