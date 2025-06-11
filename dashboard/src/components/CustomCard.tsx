import Card from "@mui/material/Card";
import CardContent from "@mui/material/CardContent";
import Typography from "@mui/material/Typography";
const CustomCard = ({ title }: { title: string }) => {
  return (
    <Card elevation={0}>
      <CardContent sx={{ height: "100%" }}>
        <Typography
          variant="h1"
          component="div"
          textAlign={"center"}
          fontWeight={700}
        >
          {title}
        </Typography>
      </CardContent>
    </Card>
  );
};

export default CustomCard;
